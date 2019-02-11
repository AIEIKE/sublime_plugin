# sublime_plugin

Main.sublime-menu:      菜单栏配置
Context.sublime-menu:   右键菜单
```
    例：[
    { "command": "translate", "caption": "翻译"},
    ]
```
Default (Windows).sublime-keymap：   快捷键设置(Windows)
```
    例：[
    {"keys": ["ctrl+t"], "command": "translate"}，
    ]
```
***
sublime_plugin.TextCommand： 文本编辑命令类
```
    run():
        sels = self.view.sel()              视图选中的区域(可以是多个, 列表)
        string = self.view.substr(sels[0])  获取第一个区域里的文本
        self.view.show_popup(string)        输出文本
```
***
+ sublime插件【翻译】
***
