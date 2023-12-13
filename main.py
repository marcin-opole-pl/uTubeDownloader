from kivymd.app import MDApp
from kivymd.uix.list import TwoLineIconListItem, IconLeftWidget
from kivymd.uix.button import MDIconButton
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
        # Display avaiable streams
        #for i in range(15):
        stream_number = 1
        for stream in url_streams:
            self.root.ids.streams_list.add_widget(
                TwoLineIconListItem(
                    DownloadIcon(),
                    text=f"Stream number {stream_number} - size: {int(stream.filesize_mb)} MB",
                    theme_text_color = 'Secondary',
                    font_style = 'H6',
                    secondary_text = str(stream)[9:-1],
                    secondary_font_style = 'Caption'
                )
            )
            stream_number += 1

    def clear_streams(self):
        '''Clear streams from the screen'''
        self.root.ids.streams_list.clear_widgets()
        self.root.ids.loading_label.text = ''

    def get_itag(self):
        '''Get itag of the stream to download'''
        self.itag = 1
        print(self.itag)


class DownloadIcon(IconLeftWidget):
    '''Download stream icon widget'''



if __name__ == '__main__':
    MainApp().run()
