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

# 设置默认shell 为fish
set-option -g default-shell /bin/fish
```

设置快捷键模式为vi, 支持`Ctrl-D/Ctrl-U`上下翻页，`/`搜索
```bash

# 设置vi模式
set -g mode-keys vi
set -g status-keys vi
```

设置[tmux-powerline](https://github.com/erikw/tmux-powerline), 支持花里胡哨
```bash

# 开启状态栏
set-option -g status on
# 设置状态栏更新间隔
set-option -g status-interval 2
# 设置tmux-powerline
set-option -g status-justify "left"
set-option -g status-left-length 60
set-option -g status-right-length 90
set-option -g status-left "#(~/usr/tmux-powerline/powerline.sh left)"
set-option -g status-right "#(~/usr/tmux-powerline/powerline.sh right)"
set-hook -g session-created 'run-shell "~/usr/tmux-powerline/powerline.sh init"' # prettifies the window-status segments

```
