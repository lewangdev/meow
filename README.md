# 研发团队协作之 Git/GitHub/GitLab 开发流程训练营

## 目标

本仓库定位于为使用 Git 标准分支开发流程的开发团队成员提供一份参考指南和训练场所

## 分支说明

### 长期分支(稳定分支)

* master

### 临时分支

* issue/\* 星号表示 issue 的编号
* feature/\* 星号表示 issue 的编号
* bugfix/\* 星号表示 issue 的编号
* hotfix/\* 星号表示issue 的编号
* release/\* 星号表示 milestone 的标题

### 开发规范

1. 认领自己准备要做的 issue 假设 issue 编号是 #99
2. 更新自己本地 master 分支代码，然后执行 `git checkout -b feather/99 master`, 这样就创建了一个名字交 feather/99 的分支
3. 提交自己的分支到 gitlab 或者 github 上，`git push -u origin feather/99`
4. 如果自己的分支开发完毕，本地测试过了，向 milestone 对应的分支发起 pull request(PR), 假设 milestone 名字是 20181028, base 分支则是 release/20181028
5. 等 milestone 中所有的 issue 的开发都完成了(开发不完则移动到下一个 milestone)，则都合并到 release/20181028, 这样 release/20181028 这个分支就是最新开发的所有功能的代码，master 是上一个最新的，后面我们流程规范了，还会对 release/20181028 分支进行各种测试，这个分支没有问题了
6. 讲 release/20181028 分支与 master 分支合并, 打个 tag，名字是 20181028, `git tag release/20181028`，进行发布
7. 进入下一个迭代和功能开发

## 标签说明

使用 Label 和 Issue 进行项目管理

### 标签分组和颜色设置

| 分组   | 前缀 |      Label      |  背景颜色 RGB 值 |
|----------|----|:-------------|------|
| 项目排期 | 项目: | 已确认，已排期，延后，开发中，测试中，已上线，待讨论 | c5def5 |
| 功能分类 | 分类: | BUG，新功能，功能增强，功能完善，文档修改    |   d4c5f9 |
| 优先级 | 优先级: | 紧急，高，低 |  e99695 |


### 参考资料

* [AMP](https://github.com/ampproject/amphtml/labels)
* [MIP](https://github.com/mipengine/mip/labels)


