import logging

logger = logging.getLogger(__name__)


class PlaylistGenerator(object):
    def __init__(self, playlist_entries=None, version=3):
        if playlist_entries == None:
            raise StandardError

        self.end_playlist = False
        self.playlist_entries = playlist_entries
        self.version = version
        self.sequence = 0
        self.duration = self.duration()

    def _generate_playlist(self):
        playlist = "{}\n{}".format(self._m3u8_header_template(), self._generate_playlist_entries())

        return playlist

    def _generate_playlist_entries(self):
        playlist = ""
        for entry in self.playlist_entries:
            playlist += "#EXTINF:{duration}\n{media}\n".format(duration=float(entry['duration']), media=(entry['name']))

        return playlist.replace(" ", "")

    def _generate(self):
        return self._generate_playlist()

    def _m3u8_header_template(self):
        header = "#EXTM3U\n#EXT-X-VERSION:{version}\n#EXT-X-MEDIA-SEQUENCE:{sequence}\n#EXT-X-TARGETDURATION:{duration}"
        return header.format(version=self.version, sequence=self.sequence, duration=self.duration).strip()

    def duration(self):
        duration_total = 0
        for entry in self.playlist_entries:
            if 'duration' in entry:
                try:
                    duration_total += float(entry['duration'])
                except Exception as e:
                    logger.exception(e)

        return duration_total

    def generate(self):
        """ This is a proxy for _generate makes it
        difficult to edit the real method for future."""
        return self._generate()
