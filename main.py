from kivymd.app import MDApp
from kivymd.uix.list import OneLineIconListItem, IconLeftWidget
from kivy.lang import Builder

from pytube import YouTube

class MainApp(MDApp):
    '''Main App class.'''
    url = 'https://www.youtube.com/'

    def build(self):
        self.theme_cls.primary_palette = 'Blue'
        self.theme_cls.accent_palette = 'Red'
        self.theme_cls.theme_style = 'Light'

        return Builder.load_file('main.kv')

    def get_streams(self):
        '''Downloads avaiable streams'''
        # Get input form user
        self.url = self.root.ids.get_url_input.text
        # Load streams from url
        url_streams = YouTube(self.url).streams
        # Display info progress
        self.root.ids.loading_label.text = 'Loaded streams: '
        # Display avaiable streams
        #for i in range(15):
        for stream in url_streams:
            self.root.ids.streams_list.add_widget(
                OneLineIconListItem(
                    IconLeftWidget(
                        icon="download-circle-outline"
                    ),
                    text=f"SIZE: {stream.filesize_mb} MB:___{str(stream)[9:-1]}",
                    theme_text_color = 'Secondary',
                    text_color = (1, 0.655, 0, 1)
                )
            )



if __name__ == '__main__':
    MainApp().run()
