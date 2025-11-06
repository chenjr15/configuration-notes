# git 技巧


## git commit 规范

参考：[Git Commit 规范 | Feflow](https://feflowjs.com/zh/guide/rule-git-commit.html)


```
feat： 新增 feature
fix: 修复 bug
docs: 仅仅修改了文档，比如 README, CHANGELOG, CONTRIBUTE等等
style: 仅仅修改了空格、格式缩进、逗号等等，不改变代码逻辑
refactor: 代码重构，没有加新功能或者修复 bug
perf: 优化相关，比如提升性能、体验
test: 测试用例，包括单元测试、集成测试等
chore: 改变构建流程、或者增加依赖库、工具等
revert: 回滚到上一个版本
```

## git log 花里胡哨版

来源：[pimping out git log - Bart's Blog](http://www.jukie.net/bart/blog/pimping-out-git-log)

设置alias
```bash 
git config --global alias.lg "log --graph --pretty=format:'%Cred%h%Creset %C(yellow)%d%Creset %s %Cgreen(%cr)%Creset' --abbrev-commit --date=relative"
```

然后`git lg`就可以啦


## git stash 只保存staged文件

来源：[](https://stackoverflow.com/a/59874960)
```
# git 2.35 (2022 Q1 )以上 
git stash --staged

```

## git 打包脚本

```bash
#!/usr/bin/bash 
project=`basename $PWD`
packageName=${project}_`git describe --tags --long`
echo $packageName
git archive HEAD --prefix=$packageName/  |gzip >"../$packageName".tar.gz
```

## 拉取pr
拉取pull request 15 并创建分支test
```bash
git fetch origin pull/15/head:test
```


## 拉取Github PR

github的pr是放在远程的`refs/pull/$PR/head`下的。

保存为git-pickpr.sh 放在PATH目录下，可以通过`git-pickpr.sh`或者 `git pickpr`使用

```sh
#!/bin/bash
set -e
#set -x

SQUASH=0
SKIP_CONFIRM=0

help(){
  echo "usage: $0 [-s|--squash] <repo> <pr>"
  echo "e.g. use squash merge to get origin repo's pull request #123: $0 -s origin 123 "
  echo "e.g. 使用squash merge方式获取origin远程的#123拉取请求: $0 -s origin 123 "
}

while getopts 'shc' flag; do
    case $flag in
    s) SQUASH=1 ;shift ;;
    h) help;exit 0;;
    c) SKIP_CONFIRM=1;;
    ?) echo unknown "$OPTARG" "$OPTVALUE"; help; exit 1;;
    *) help;exit 1;;
    esac
done
if [ "$#" -lt 2 ]; then
  help
  exit 1
fi
REPO=$1
PR=$2
echo -n searching repo="$REPO" pr="$PR" " "
if [ "$SQUASH" -eq 1 ] ; then
  echo using squash merge\(merge without commit\): \`git merge --squash\` instead of git rebase
else
  echo 
fi
REPO_URL=$(git remote  get-url $REPO )


# ls-remote 查找对应分支
last_commit=$(git ls-remote --refs "$REPO" refs/pull/$PR/head |cut -f 1 )
git fetch "$REPO" "$last_commit"
git log HEAD.."$last_commit"

if [ "$SKIP_CONFIRM" -ne 1 ]; then
        read -p "Press Enter to continue, Ctrl-C to exit."
fi

set -x
if [ "$SQUASH" -eq 1 ] ; then
  git merge --squash "$last_commit"
else
  git rebase "$last_commit"
fi
set +x
```
