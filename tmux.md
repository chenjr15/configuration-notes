配置文件路径

```bash
vim ~/.tmux.conf
```

重载变更:

`C-B :`然后输入命令

```bash
source ~/.tmux.conf
```


开启鼠标(触屏设备就是直接点)支持(切换window/panel, 重设大小, 滚屏等)

```bash
setw -g mouse-resize-pane on
setw -g mouse-select-pane on
setw -g mouse-select-window on
setw -g mode-mouse on
```
