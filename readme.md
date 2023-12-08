# 快速获得青年大学习完成页

> **Warning**  
> 已归档，暂不维护

[~~敷衍网址~~](https://pizerolol.github.io/test/)

> **Note**  
> 目前无法使用，据说是因为青年大学习把 Github Action 的 ip ban 了

该项目使用cc0方式开源。

这个项目是我第一次尝试使用github action和github pages来搭建一个定时更新的网站。
虽说在gitee的时候也尝试使用bot的方式的进行通知实现来着，但是效果不好。

制作这个项目的原因是我讨厌各种奇奇怪怪的指标，以各种理由不让人回家或者打扰别人。

该学习的还是得学，但是我认为我有权力拒绝他人指指点点我学习。

## 使用方法

~~由于 Github Action 的 ip 被屏蔽，被迫学一些奇奇怪怪但是非常好用的应用部署方式。~~

### 生成 html 文件

```bash
python -m venv .venv
source .venv/bin/.venv/bin/activate
pip install -r requirements.txt
python main.py
```

用 `python` 自带的 `venv` 模块生成一个叫做 `.venv` 的目录，使用里面的设置。
然后安装依赖，最后执行 `main.py` 来爬取青年大学习完成图片。
文件保存在 `public/` 目录下。

`Windows` 自己百度 `python venv`。

### 命令行启动服务

```bash
python -m venv .venv
source .venv/bin/.venv/bin/activate
pip install -r server-requirements.txt
uvicorn server:app --port 端口 --host 访问目标ip
```

和生成 html 文件基本一样，只不过安装的依赖和执行的文件不同。
如果嫌下载慢可以去 `MirrorZ` 或者其他镜像站找个 `pypi` 镜像。

把 `--port 端口 --host 访问的目标ip` 去掉默认允许通过 `127.0.0.1:8000` 来访问。
这里 `访问目标ip` 描述的可能不是很准确，意思就是访问者可以通过访问哪个ip来访问该服务。

### `Dockerfile` 启动服务

> **Warnning**  
> 目前未测试

```bash
docker build -t xxx:yyy .
docker run -p 主机端口:8000 --name 名称 -d --restart unless-stopped xxx:yyy
```

自己构建，然后启动服务。
可惜不知道为什么，暂时不能使用，不过欢迎提 issuses。

### `Systemd` 启动服务

由于我使用的是用户权限的 `systemd`，这里以用户模式为例。

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r server-requirements.txt
```

使用你心仪的文本编辑器编辑 example/systemd/start_service.sh，
自行修改上面的端口和虚拟环境地址。
虚拟环境地址就是你刚 `-m venv` 后面的地址，如果你是复制粘贴的那就是`.venv`。

使用你心仪的文本编辑器编辑 `example/systemd/qinnian.service`。
将 `clone目录` 换成你克隆的地址，如果不知道，那你 `pwd` 一下看看。

```bash
mkdir -p ~/.config/systemd/user
cp example/systemd/qinnian.service ~/.config/systemd/user/
systemctl --user daemon-reload
systemctl --user start qinnian
```

创建 `systemctl` 用户模式目录，将刚刚编辑好的 `service` 文件拷贝到刚刚创建的目录下。
然后重启 `systemd` 用户模式，最后启动。
你要是想开机自动启动可以使用以下命令：

```bash
systemctl --user enable qinnian
```
