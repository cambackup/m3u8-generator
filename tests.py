import unittest
from m3u8_generator import PlaylistGenerator


class TestPlaylistCase(unittest.TestCase):
    def setUp(self):
        self.playlist_entries = [
            {
                'name': 'awesome_video_001.mp4',
                'duration': '10.0',
                'start': '0.00',
                'end': '10.0'

            },
            {
                'name': 'awesome_video_002.mp4',
                'duration': '10.0',
                'start': '10.0',
                'end': '20.0'

            },
            {
                'name': 'awesome_video_003.mp4',
                'duration': '10.0',
                'start': '20.00',
                'end': '30.01'

            },
            {
                'name': 'awesome_video_004.mp4',
                'duration': '10.0',
                'start': '30.00',
                'end': '40.0'

            }
        ]

    def test_playlist_durataion_generation(self):
        """When a user provides a playlist it needs to count the total duration."""
        playlist_duration = PlaylistGenerator(playlist_entries=self.playlist_entries).duration
        self.assertEquals(playlist_duration, 40, msg="Ensure duration is counted")

    def test_playlist_header_generation(self):
        """Make sure there is the EXTM3U on the firstline"""
        header = PlaylistGenerator(self.playlist_entries, version=3)._m3u8_header_template()
        self.assertTrue('EXTM3U' in header)

    def test_playlist_header_version_generation(self):
        """Make sure there is the version identifier"""
        header = PlaylistGenerator(self.playlist_entries, version=3)._m3u8_header_template()
        self.assertTrue('EXT-X-VERSION:3' in header)

    def test_playlist_header_duration_generation(self):
        """Make sure there is the duration identifier """
        header = PlaylistGenerator(self.playlist_entries, version=3)._m3u8_header_template()
        self.assertTrue('EXT-X-TARGETDURATION:40' in header)

    def test_playlist_header_sequence_generation(self):
        """Make sure there is the sequence"""
        header = PlaylistGenerator(self.playlist_entries, version=3)._m3u8_header_template()
        self.assertTrue('EXT-X-MEDIA-SEQUENCE:0' in header)

    def test_end_of_playlist(self):
        """Ensures that the end playlist is included"""
        playlist = PlaylistGenerator(self.playlist_entries, version=3).generate()
        self.assertTrue('#EXT-X-ENDLIST' in playlist)

    def test_end_of_is_included(self):
        """Ensures that the end playlist is included"""
        playlist = PlaylistGenerator(self.playlist_entries, version=3).generate()
        self.assertTrue('#EXT-X-ENDLIST' in playlist)

    def test_end_of_is_not_included(self):
        """Ensures that the end playlist is included"""
        playlist = PlaylistGenerator(self.playlist_entries, version=3)
        playlist.end_playlist = False
        self.assertTrue('#EXT-X-ENDLIST' not in playlist.generate())

if __name__ == '__main__':
    unittest.main()
