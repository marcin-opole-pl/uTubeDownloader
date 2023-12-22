from kivymd.app import MDApp
from kivymd.uix.list import TwoLineListItem
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


class ParsedStream(TwoLineListItem):
    '''Stream object after conversion'''
    def __init__(self, value, **kwargs):
        super(ParsedStream, self).__init__(**kwargs)

        #Get stream size
        self.stream_size = int(value.filesize_mb)

        # Clean stream info
        stream_info = str(value)[9:-1].replace('"','')

        # Convert stream to a list
        stream_as_list = stream_info.split(' ')

        #Get itag and type from stream
        for element in stream_as_list:
            if element.startswith('itag='):
                self.stream_itag = element[5:]

        for element in stream_as_list:
            if element.startswith('type='):
                self.stream_type = element[10:]


        self.text=f"Stream size: {self.stream_size} MB"
        self.secondary_text = stream_info

    def get_itag(self):
        '''Get itag of the stream to download'''
        print(self.stream_itag)



if __name__ == '__main__':
    MainApp().run()
