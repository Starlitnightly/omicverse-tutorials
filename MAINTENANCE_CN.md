# 维护与子模块同步指南

当前 `omicverse-tutorials` 是一个独立仓库，同时也被主仓库 `omicverse` 作为 git 子模块引用。

## 1. 仓库关系

- 独立仓库：`analysis/omicverse-tutorials`
- 主仓库：`analysis/omicverse`
- 主仓库中的子模块路径：`omicverse/omicverse_guide`

推荐工作流：

1. 先在 `omicverse-tutorials` 独立仓库中修改文档。
2. 在 `omicverse-tutorials` 中提交并推送。
3. 回到 `omicverse` 主仓库更新子模块指针。

## 2. 在 `omicverse-tutorials` 中日常开发

```bash
cd /Users/fernandozeng/Desktop/analysis/omicverse-tutorials
git status
git checkout main
git pull origin main
```

修改完成后：

```bash
git add -A
git commit -m "Describe the tutorial update"
git push origin main
```

## 3. 把最新提交同步回 `omicverse`

在独立仓库推送后，回到主仓库更新子模块指针：

```bash
cd /Users/fernandozeng/Desktop/analysis/omicverse
git submodule update --init --recursive
cd omicverse_guide
git checkout main
git pull origin main
cd ..
git add omicverse_guide .gitmodules
git commit -m "Update omicverse_guide submodule"
git push
```

如果 `.gitmodules` 没有变化，只需要 `git add omicverse_guide`。

## 4. 其他人在主仓库中如何同步子模块

```bash
cd /Users/fernandozeng/Desktop/analysis/omicverse
git pull --recurse-submodules
git submodule update --init --recursive
```

如果子模块目录已经存在，但版本落后：

```bash
cd /Users/fernandozeng/Desktop/analysis/omicverse/omicverse_guide
git checkout main
git pull origin main
cd ..
git add omicverse_guide
```

## 5. 从零克隆主仓库

```bash
git clone --recurse-submodules https://github.com/Starlitnightly/omicverse.git
```

如果之前没有带子模块：

```bash
cd omicverse
git submodule update --init --recursive
```

## 6. 常见问题

- 不要只在 `omicverse` 里更新子模块指针，却忘了先把真正的文档改动提交推送到 `omicverse-tutorials`。
- 不要长期直接在 `omicverse/omicverse_guide` 里维护文档，`analysis/omicverse-tutorials` 才是主开发仓库。
- 如果子模块目录处于 detached HEAD，先在子模块里执行 `git checkout main`，再继续 `git pull`。
