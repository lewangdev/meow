# 研发团队协作之 Git/GitHub/GitLab 开发流程训练营

## 目标

本仓库定位于为使用 Git 标准分支开发流程的开发团队成员提供一份参考指南和训练场所

## 分支说明

### 长期分支(稳定分支)

* master

### 临时分支

* feature/\* 星号表示issue的编号
* bugfix/\* 星号表示issue的编号
* hotfix/\* 星号表示issue的编号
* release/\* 星号表示milestone的标题

### 分支规范

1. 认领自己准备要做的issue，加上 issue 编号是 #99
2. 更新自己本地master分支代码，然后执行 git checkout -b feather/99 master, 这样就创建了一个名字交 feather/99 的分支
3. 提交自己的分支到 gitlab 或者 github 上，git push -u origin feather/99
4. 如果自己的分支开发完毕，本地测试过了，向milestone对应的分支发起 pull request(PR), 假设 milestone 名字是 20181028, 分支则是 release/20181028
5. 等milestone中所有的 issue 的开发都完成了，则都合并到 release/201828, 这样 release/201828 这个分支就是最新开发的所有功能的代码，master 是上一个最新的，后面我们流程规范了，还会测是这个分支，这个分支没有问题了，打个tag，名字是 release/201828, git tag release/201828，进行发布
6. release/201828 最后会和 master 分支合并，保持 master 最新，并且一直可用
7. 进入下一个迭代和功能开发
