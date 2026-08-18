# DockerHomework

一个使用 Flask、Docker 和 Docker Compose 的简单 Web 应用。访问首页后点击按钮，会请求 `/api/hello` 并显示 `Hello World`。

## 本地运行

```bash
docker compose up --build
```

然后访问 <http://localhost:8000>。

## 使用 GitHub Actions 自动构建镜像

工作流位于 `.github/workflows/deploy.yml`。每次推送到 `main` 分支时，它会：

1. 安装依赖并验证 `/api/hello`。
2. 构建 Docker 镜像，并推送到 GitHub Container Registry（GHCR）。

无需配置部署服务器或 SSH Secrets。推送完成后，可在仓库的 **Packages** 页面查看镜像；标签包含 `latest` 和本次提交的 SHA。也可在 Actions 页面手动运行 **Build Flask image**。
