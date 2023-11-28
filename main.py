from kivymd.app import MDApp

from pytube import YouTube

class MainApp(MDApp):
    '''Main App class.'''
    url = 'https://www.youtube.com/'

    def build(self):
        self.theme_cls.primary_palette = 'Orange'

    def get_streams(self):
        '''Downloads avaiable streams'''
        # Display info on progress
        self.root.ids.loading_label.text = 'Loading streams'
        # Get input form user
#        self.url = self.root.ids.get_url_input.text
        # Load streams from url
#        url_streams = YouTube(self.url).streams
        # Display info progress
#        self.root.ids.loading_label.text = 'Streams loaded'
        # Display avaiable streams
#        for elem in url_streams:
#            print(elem)



if __name__ == '__main__':
    MainApp().run()
