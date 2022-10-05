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
