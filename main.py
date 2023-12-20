from kivymd.app import MDApp
from kivymd.uix.list import TwoLineIconListItem
from kivy.lang import Builder

from pytube import YouTube

class MainApp(MDApp):
    '''Main App class.'''
    url = 'https://www.youtube.com/'
    itag = 0

    def build(self):
        self.theme_cls.primary_palette = 'Blue'
        self.theme_cls.accent_palette = 'Red'
        self.theme_cls.theme_style = 'Light'

        return Builder.load_file('main.kv')

    def get_streams(self):
        '''Downloads avaiable streams'''
        # Get url form user
        self.url = self.root.ids.get_url_input.text

        # Load streams from url
        url_streams = YouTube(self.url).streams

        # Display info progress
        self.root.ids.loading_label.text = 'Loaded streams: '

        # Convert url_streams into list of parsed streams
        list_of_streams = []
        for element in url_streams:
            stream = ParsedStream(element)
            list_of_streams.append(stream)

        # Display avaiable streams
        for stream in list_of_streams:
            self.root.ids.streams_list.add_widget(stream)


    def clear_streams(self):
        '''Clear streams from the screen'''
        self.root.ids.streams_list.clear_widgets()
        self.root.ids.loading_label.text = ''


class ParsedStream(TwoLineIconListItem):

    def __init__(self, value, **kwargs):
        super(ParsedStream, self).__init__(**kwargs)

        self.text=f"Stream size: {int(value.filesize_mb)} MB"
        self.secondary_text = str(value)[9:-1]

    def get_itag(self):
        '''Get itag of the stream to download'''
        print(self.text)



if __name__ == '__main__':
    MainApp().run()
