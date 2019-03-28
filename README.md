<p align="center">
    <img src="MeowLogo.png" />
</p>

<p align="center">
    <a href="https://github.com/thisiswangle/meow/graphs/contributors">
        <img src="https://img.shields.io/github/contributors/thisiswangle/meow.svg" >
    </a>
    <a href="https://github.com/thisiswangle/meow">
        <img alt="GitHub repo size" src="https://img.shields.io/github/repo-size/thisiswangle/meow.svg">
    </a>
    <a href="https://github.com/thisiswangle/meow/issues">
        <img alt="GitHub issues" src="https://img.shields.io/github/issues/thisiswangle/meow.svg">
    </a>
</p>

# Meow

这是一个面向新手的 Git/GitHub/GitLab 团队协作修炼场所，玩一次即可熟悉 Git/GitLab/GitHub 的使用。不过在开启学习之前，请至少准备好撸猫皂片一张，没有猫的，可以去 [unsplash](https://unsplash.com/search/photos/cat) 使用关键词 `cat` 或者 `kitten` 搜索，一定会找到萌到你的猫咪照，meow~

### 目标

* 为使用 Git/GitHub/GitLab 协作的团队中的新手成员提供一份参考指南和训练场所。
* 项目本身很简单，不要求参与的人贡献代码，不需要编程技能，任何想熟悉 Git/GitHub/Gitlab 的人都可以参加。
* 通过这个项目可以学会:
    * Git 从克隆项目(fork/clone)，创建分支(branch)，提交和同步修改(pull/push)，到发起合并请求(PR)的流程;
    * 使用 GitHub/GitLab 进行项目协作开发管理。

### 分支说明

#### 长期分支(稳定分支)

* master

#### 临时分支

* issues/{issue-id}，新建分支优先使用的命名约定 
* bugfix/{issue-id}，为了区分描述的问题是BUG，可以使用 bugfix 分支命名约定
* hotfix/{issue-id}，紧急情况的线上修复，可以使用 hotfix 分支命名约定
* releases/{milestone-title}，项目定期发布的分支命名约定

#### Git 分支规范

0. fork 项目到自己的空间，如果是自己是 GitLab 的项目成员或者 GitHub 的项目协作成员，可以不用做这一步
1. 认领自己准备要做的 issue， 假设 issue 编号是 #99
2. 更新自己本地 master 分支代码: `git pull`
3. 创建一个名字叫 issues/99 的分支: `git checkout -b issues/99 master`
4. 开始功能开发，每一个 commit 都要带上自己的 issue id，完成之后提交自己的改动，如 `git commit -m '#99 昨天撸的那只猫的照片'`
5. 提交自己的分支到 GitLab 或者 GitHub 上，`git push -u origin issues/99`
6. 如果自己的分支开发完毕，本地测试过了，向 milestone 对应的分支发起 pull request(PR)，假设 milestone 名字是 20181028，base 分支则是 releases/20181028
7. 等 milestone 中所有的 issue 的开发都完成了(开发不完则移动到下一个 milestone)，则都合并到 releases/20181028，这样 releases/20181028 这个分支就是最新开发的所有功能的代码，master 是上一个最新的，后面我们流程规范了，还会对 releases/20181028 分支进行各种测试，这个分支没有问题了
8. 将 releases/20181028 分支与 master 分支合并，打个 tag，名字是 20181028，`git tag 20181028`，进行发布
9. 进入下一个迭代和功能开发

### 项目管理

使用 Label 和 Issue 进行项目管理

#### 标签分组和颜色设置

| 分组     | 前缀   |      Label                                           | 背景颜色 RGB 值 |
|----------|--------|:-----------------------------------------------------|-----------------|
| 项目排期 | 项目   | 已确认，已排期，延后，开发中，测试中，已上线，待讨论 | c5def5          |
| 功能分类 | 分类   | BUG，新功能，功能增强，功能完善，文档修改            | d4c5f9          |
| 优先级   | 优先级 | 紧急，高，低                                         | e99695          |

* [查看彩色的标签](https://github.com/thisiswangle/meow/labels)
* [查看使用了标签的 Issue 列表](https://github.com/thisiswangle/meow/issues?q=is%3Aissue+is%3Aclosed)

#### 项目发布

每周二和周四发布，版本号为发布日的日期，格式为 `yyyyMMdd`

### 参与项目

0. 角色扮演(如果是自己是 GitLab 的项目成员或者 GitHub 的项目协作成员)
    * 新建一个 issue，为这个 issue 选好对应的标签，项目排期，功能分类，优先级至少各有一个标签
    * 把 issue 分配给自己
    * 把 issue 添加到对应的 milestone
1. 上传至少一张猫照
    * 创建一个目录
    * 尽量使用有意义的名字且不要出现空格
    * 目录名称可使用你的 GitHub ID 或者其他社交平台上非中文的 ID 来命名
    * 影响排序的目录命名 (例如 AAAA.Folder，0.Folder，111Folder) 会被 Close Pull Request
    * 如果需要在你的文件夹内创建描述文件,请尽量使用 Markdown 语法来编写
    * 将猫照放在这个目录下面，照片尽量压缩，Size 不要太大，清晰度不要太低
2. 使用 Git 分支规范完成任务
3. 在 PR 被合并之后，关闭 issue
4. 请仔细阅读 [CONTRIBUTING](CONTRIBUTING.md)

### License

本项目采用知识共享署名-非商业性使用-相同方式共享 4.0 国际许可协议进行许可。

### 参考资料

* [Learn Git Branching](https://learngitbranching.js.org/)
* [Git Doc](https://git-scm.com/doc)
* [AMP](https://github.com/ampproject/amphtml/labels)
* [MIP](https://github.com/mipengine/mip/labels)
* [Dress](https://github.com/komeiji-satori/Dress)

