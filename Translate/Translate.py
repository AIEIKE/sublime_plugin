import json
import sublime
import sublime_plugin
from urllib import request
from urllib import parse


url = 'http://fanyi.youdao.com/translate'


class TranslateCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        sel = self.view.sel()
        if len(sel) > 0:
            sel = sel[0]
        text = self.view.substr(sel)
        words = text.replace('\n', ' ')
        data = {
            'doctype': 'json',
            'type': 'AUTO',
            'i': words
        }
        params = parse.urlencode(data)
        zurl = url + '?' + params
        with request.urlopen(zurl) as f:
            r = f.read().decode()
        d = json.loads(r)
        s = d['translateResult'][0][0]['tgt']
        self.view.show_popup(s)
