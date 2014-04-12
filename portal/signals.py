import urllib2
import shutil

import lambdaproject.settings as settings

def get_remote_filesize(sender, instance, **kwargs):
    instance.size = _get_remote_filesize_for_url(instance.url)

def _get_remote_filesize_for_url(url):
    try:
        request = urllib2.Request(url)
        request.get_method = lambda: 'HEAD'

        response = urllib2.urlopen(request)
        return response.info().getheader('content-length')
    except:
        pass

def purge_files(sender, instance, **kwargs):
    shutil.rmtree(settings.ENCODING_OUTPUT_DIR + instance.slug, True)
    if instance.originalFile:
        instance.originalFile.delete(False)
