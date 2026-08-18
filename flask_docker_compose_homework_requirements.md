# Flask + Docker + Docker Compose 作业要求

## 作业目标

完成一个简单的 Web 项目：

- 使用 **Python + Flask API** 创建网页
- 网页上有一个按钮
- 点击按钮后调用后端 API
- 后端返回 `Hello World`
- 将项目打包成 **Docker 镜像**
- 最后使用 **Docker Compose** 启动整个项目

---

## 第一部分：Python + Flask API

### 1. 创建项目目录

- [ ] 创建项目文件夹，例如：

```text
flask-docker-homework/
```

- [ ] 进入项目目录
- [ ] 创建 Python 虚拟环境
- [ ] 安装 Flask

例如：

```bash
python -m venv venv
pip install flask
```

### 2. 创建 Flask 后端

- [ ] 创建 `app.py`
- [ ] 创建 Flask Application
- [ ] 创建首页 `/`
- [ ] 创建 API，例如：

```text
GET /api/hello
```

- [ ] API 返回：

```text
Hello World
```

或：

```json
{
  "message": "Hello World"
}
```

### 3. 创建前端网页

- [ ] 创建：

```text
templates/index.html
```

- [ ] 网页中添加一个按钮，例如：

```text
Get Hello
```

- [ ] 使用 JavaScript `fetch()` 请求：

```text
/api/hello
```

- [ ] 点击按钮后，将 API 返回的 `Hello World` 显示在网页上

### 4. 本地测试

- [ ] 启动 Flask：

```bash
python app.py
```

- [ ] 浏览器访问：

```text
http://localhost:5000
```

- [ ] 确认网页能够正常打开
- [ ] 点击按钮
- [ ] 确认网页显示：

```text
Hello World
```

### 5. 创建依赖文件

- [ ] 创建 `requirements.txt`

例如：

```text
Flask
```

或者：

```bash
pip freeze > requirements.txt
```

完成第一部分后，项目结构大致应该是：

```text
flask-docker-homework/
├── app.py
├── requirements.txt
└── templates/
    └── index.html
```

---

## 第二部分：将项目打包成 Docker

### 6. 修改 Flask 启动配置

- [ ] 确保 Flask 监听：

```python
host="0.0.0.0"
```

例如：

```python
app.run(host="0.0.0.0", port=5000)
```

注意这里不能只监听 `127.0.0.1`，否则 Docker 容器外部无法通过映射端口访问 Flask。

### 7. 创建 Dockerfile

- [ ] 在项目根目录创建：

```text
Dockerfile
```

- [ ] Dockerfile 至少完成以下操作：

```text
选择 Python 基础镜像
        ↓
设置工作目录
        ↓
复制 requirements.txt
        ↓
安装 Python 依赖
        ↓
复制项目代码
        ↓
启动 Flask
```

### 8. 构建 Docker 镜像

- [ ] 执行：

```bash
docker build -t flask-hello .
```

- [ ] 查看镜像是否成功生成：

```bash
docker images
```

### 9. 运行 Docker 容器

- [ ] 启动容器，例如：

```bash
docker run -p 5000:5000 flask-hello
```

其中：

```text
5000:5000
  ↑    ↑
主机   容器
端口   端口
```

### 10. 测试 Docker 版本

- [ ] 浏览器访问：

```text
http://localhost:5000
```

- [ ] 点击按钮
- [ ] 确认仍然能够显示：

```text
Hello World
```

- [ ] 也可以直接测试 API：

```bash
curl http://localhost:5000/api/hello
```

完成第二部分后，项目结构大致为：

```text
flask-docker-homework/
├── app.py
├── Dockerfile
├── requirements.txt
└── templates/
    └── index.html
```

---

## 第三部分：使用 Docker Compose

### 11. 创建 Docker Compose 文件

- [ ] 在项目根目录创建：

```text
compose.yaml
```

或者：

```text
docker-compose.yml
```

- [ ] 定义一个 Flask 服务，例如：

```yaml
services:
  web:
    build: .
    ports:
      - "5000:5000"
```

### 12. 使用 Docker Compose 构建项目

- [ ] 执行：

```bash
docker compose build
```

### 13. 使用 Docker Compose 启动项目

- [ ] 执行：

```bash
docker compose up
```

或者后台运行：

```bash
docker compose up -d
```

### 14. 测试 Docker Compose

- [ ] 浏览器访问：

```text
http://localhost:5000
```

- [ ] 点击按钮
- [ ] 确认显示：

```text
Hello World
```

- [ ] 测试 API：

```bash
curl http://localhost:5000/api/hello
```

### 15. 停止 Docker Compose

- [ ] 执行：

```bash
docker compose down
```

---

## 最终需要提交的文件

```text
flask-docker-homework/
├── app.py
├── Dockerfile
├── compose.yaml
├── requirements.txt
└── templates/
    └── index.html
```

## 最终验收标准

- [ ] `python app.py` 可以启动项目
- [ ] 浏览器能够打开网页
- [ ] 网页上存在按钮
- [ ] 点击按钮后调用 Flask API
- [ ] API 返回 `Hello World`
- [ ] `docker build` 可以成功构建镜像
- [ ] `docker run` 可以正常运行项目
- [ ] `docker compose up` 可以正常运行项目
- [ ] 三种启动方式下网页功能完全一致
