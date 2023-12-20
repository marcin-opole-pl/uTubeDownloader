from kivymd.app import MDApp
from kivymd.uix.list import TwoLineIconListItem
from kivy.lang import Builder

from pytube import YouTube

class MainApp(MDApp):
    '''Main App class.'''
    url = 'https://www.youtube.com/'
    stream = 0

    def build(self):
        self.theme_cls.primary_palette = 'Blue'
        self.theme_cls.accent_palette = 'Red'
        self.theme_cls.theme_style = 'Light'

        return Builder.load_file('test.kv')

    def get_streams(self):
        # Display info progress
        self.root.ids.loading_label.text = 'Loaded streams: '
        # Display avaiable streams
        list_of_streams = []
        for i in range(5):
            stream = ParsedStream(i)
            list_of_streams.append(stream)
        for stream in list_of_streams:
            self.root.ids.streams_list.add_widget(stream)


    def clear_streams(self):
        '''Clear streams from the screen'''
        self.root.ids.streams_list.clear_widgets()
        self.root.ids.loading_label.text = ''


class ParsedStream(TwoLineIconListItem):

    def __init__(self, value, **kwargs):
        super(ParsedStream, self).__init__(**kwargs)
        self.text = str(value)

    def get_itag(self):
        '''Get itag of the stream to download'''
        print(self.text)

if __name__ == '__main__':
    MainApp().run()
