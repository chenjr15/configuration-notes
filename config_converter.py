#!/usr/bin/python3
"""
配置文件互转工具
author: chenjr15

"""

from sys import stderr, stdin, stdout
from io import StringIO
import json
from collections.abc import Generator
from collections import namedtuple
import copy
import yaml

import click

KVPair = namedtuple('KeyValue', ('key', 'value'))
KVPair.__repr__ = lambda kv: f"{kv.key}={kv.value}"
KVPair.__str__ = KVPair.__repr__


class Properties:
    def __init__(self, config_filename: str = None, configs: dict = None):

        self.configs = {}
        if configs:
            self.configs = configs
        if config_filename:
            with open(config_filename, encoding='utf8') as f:
                self.readstream(f)

    def __iter__(self):
        frozen = copy.deepcopy(self.configs)

        def dfs_visit(tree: dict, key_prefix=[]):
            for key, val in tree.items():
                full_path = [*key_prefix, key]
                if isinstance(val, dict):
                    yield from dfs_visit(val, full_path)
                else:
                    yield KVPair('.'.join(full_path), val)
                    continue
        return dfs_visit(frozen)

    def readstream(self, config_stream) -> KVPair:
        lastline = ''
        for line in config_stream:
            line: str = line.strip()
            if not line or line[0] == '#':
                # 注释直接pass
                continue
            if line[-1] == '\\':
                # 多行的情况,附加到lastline中并直接continue掉
                lastline += line[:-1]
                continue
            elif lastline:
                # 多行结束，拼接多行的内容并清空lastline
                line = lastline+line
                lastline = ''
            # print('reading:', line, line.split('=', maxsplit=1))
            fullkeys, value = line.split('=',  maxsplit=1)
            self.set(fullkeys, value)
        return self.configs

    def writestream(self, out_stream: StringIO):
        for kv in self:
            print(kv, file=out_stream)

    def set(self, key: str, value):
        """set key to value

        Args:
            key (str): full key like 'a.b.c'
            value (any): just the value
        """
        if not key:
            raise KeyError("Empty key is not allow!")
        if isinstance(key, (list, tuple, Generator)):
            keys = tuple(key)
            *forefather, father = keys
        else:
            *forefather, father = key.split('.')

        parent = self.get(forefather, True)
        parent[father] = value

    def get(self, key, setdefault=False):
        """get section return the section of configs

        Args:
            key (str/list/tuple/Generator): key path to find ,like "keya.keyb.keyc"; also accepts list, tuple and generator.
            setdefault (bool, optional): is set True, the not found key will be set to {} as default value. Defaults to False, raise KeyError for key that does not exist.

        Returns:
            value of key
        """
        if not key:
            raise KeyError("Empty key is not allow!")
        keys = []
        if isinstance(key, (list, tuple, Generator)):
            keys = tuple(key)
        else:
            keys = key.split('.')
        configs = self.configs
        for key in keys:
            if setdefault:
                configs = configs.setdefault(key, {})
            else:
                configs = configs[key]
        return configs

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, value):
        return self.set(key, value)

    def __repr__(self):
        return repr(self.configs)

    def __str__(self):
        return '\n'.join(str(kv) for kv in self)


def test():
    jp = Properties('config.properties')

    print(jp)
    print(json.dumps(jp.configs, ensure_ascii=False, indent=2))
    print(yaml.dump(jp, allow_unicode=True))

    def getkeys():
        return ['xxx.fff.kkk', (1, 2, 4), (c for c in 'string'), '', [], ['']]

    def test_get():
        test_keys = getkeys()
        for key in test_keys:
            print('> testing get :', key)
            try:
                v = jp.get(key)
                print('got', v)
            except KeyError as e:
                print('key not found', key, e)

    def test_set():
        test_keys = getkeys()
        for key in test_keys:

            print('> testing set :', key)
            try:
                jp.set(key, f'VALUE of {key}')
            except KeyError as e:
                print('key not found', key, e)
    test_get()
    test_set()
    test_get()


decoders = {
    'json': json.load,
    'properties': Properties().readstream,
    'yml': yaml.load,
    'yaml': yaml.load
}


def yml_encoder(obj, fp): return yaml.dump(obj, fp, allow_unicode=True)


def proper_encoder(obj, fp):
    p = Properties()
    p.configs = obj
    p.writestream(fp)


encoders = {
    'json': lambda obj, fp: json.dump(obj, fp, ensure_ascii=False, indent=2),
    'properties': proper_encoder,
    'yml': yml_encoder,
    'yaml': yml_encoder
}


def get_type(select: str = None, filename: str = None, default: str = None):
    ftype = select
    if not ftype and filename != '-' and filename is not None:
        _, ftype = filename.split('.', maxsplit=1)
    if not ftype:
        ftype = default
    return ftype


@click.command(name='ConfigConvert')
@click.option('--in-type', type=str, help='file type of input file, auto dectect from input filename(properties for -)')
@click.option('--out-type', type=str, help='file type of output file, auto dectect from output filename(yaml for -)')
@click.option('-i', '--infile', type=str, default='-', help='input filenmae, default is - (stdin)')
@click.option('-o', '--outfile', type=str, default='-', help='output filenmae, default is - (stdout)')
def cmd(infile: str = '-', outfile: str = '-', in_type: str = None, out_type: str = None):
    """Config File Converter 配置文件互转工具 

    supported formats: Java properties (.properties),Json(.json) and yaml(.yml,.yaml)
    """
    infp = click.open_file(infile, encoding='utf8')
    outfp = click.open_file(outfile, 'w', encoding='utf8')

    in_type = get_type(in_type, infile, 'properties')
    out_type = get_type(out_type, outfile, 'yml')

    decode = decoders[in_type]
    encode = encoders[out_type]

    configs = decode(infp)
    encode(configs, outfp)


if __name__ == '__main__':
    cmd()
    # cmd('config.properties', 'config.yaml')
