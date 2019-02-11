# sublime_plugin

Main.sublime-menu:      菜单栏配置<br>
Context.sublime-menu:   右键菜单<br>
```
    例：[
    { "command": "translate", "caption": "翻译"},
    ]
```
Default (Windows).sublime-keymap：   快捷键设置(Windows)<br>
```
    例：[
    {"keys": ["ctrl+t"], "command": "translate"}，
    ]
```
***
sublime_plugin.TextCommand： 文本编辑命令类<br>
    run:
        sels = self.view.sel()              视图选中的区域（可以是多个）<br>
        string = self.view.substr(sels[0])  获取第一个区域里的文本<br>
        self.view.show_popup(string)        输出文本<br>
***
+ sublime插件【翻译】
***
