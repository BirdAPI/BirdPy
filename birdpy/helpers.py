import time
import urllib2
import traceback
import re
import os
import socket
import random
import platform

def get_lan_ip(test_ip="8.8.8.8", test_port=80):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect((test_ip,int(test_port)))
    ip = s.getsockname()[0]
    s.close()
    return ip

def wait_for_network(sleep_interval, timeout):
    try:
        print get_lan_ip()
    except:
        if float(timeout) > 0:
            time.sleep(float(sleep_interval))
            wait_for_network(sleep_interval, float(timeout) - float(sleep_interval))

def download_file(url, folder):
    try:
        fname = None
        headers = { 'User-Agent' : 'Mozilla/5.0' }
        req = urllib2.Request(url, None, headers)
        response = urllib2.urlopen(req)
        data = response.read()
        if 'Content-Disposition' in response.info().headers:
            cd = response.info().headers['Content-Disposition']
            regex = "filename *= *(^[ ]+)"
            m = re.search(regex, cd)
            if m:
                fname = m.group(0)
        if fname is None:
            fname = os.path.basename(url)
            if '?' in fname:
                fname = fname[:fname.find('?')]
        print "FILENAME IS:", fname
        with open(os.path.join(folder, fname), 'w') as f:
            f.write(data)
        return True
    except:
        print traceback.format_exc()
        return False

def round_to_even(num):
    return int(num / 2) * 2

def gmt_timestamp_for_datetime(dt):
    """
    Pass in a datetime object, and get back a gmt timestamp
    for use in cookies and headers.
    """
    if dt is None:
        return None
    return time.strftime("%a, %d-%b-%Y %H:%M:%S GMT", gmtime_for_datetime(dt))

def gmtime_for_str(str_date):
    """
    Pass in a datetime string, and get back time.gmtime
    """
    return time.gmtime(time.mktime(time.strptime(str_date, "%a, %d-%b-%Y %H:%M:%S GMT"))) if str_date is not None else None

def expires_timestamp(days=None, hours=None, minutes=None, seconds=None):
    """
    Get an expires header timestamp for the specified time from now
    """
    expires = time.time()
    if days:
        expires += days * 3600 * 24
    if hours:
        expires += hours * 3600
    if minutes:
        expires += minutes * 60
    if seconds:
        expires += seconds
    return time.strftime("%a, %d-%b-%Y %H:%M:%S GMT", time.gmtime(expires))

def gmtime_for_datetime(dt):
    """
    Pass in a datetime object, and get back time.gmtime
    """
    return time.gmtime(time.mktime(time.strptime(dt.strftime("%Y-%m-%d %H:%M:%S"), "%Y-%m-%d %H:%M:%S"))) if dt is not None else None

def munge(string):
    return unicode(string).encode('utf-8', 'xmlcharrefreplace')

def get_current_ms():
    return int(round(time.time() * 1000))

def random_mac():
    mac = [
        random.randint(0x00, 0xff),
        random.randint(0x00, 0xff),
        random.randint(0x00, 0xff),
        random.randint(0x00, 0xff),
        random.randint(0x00, 0xff),
        random.randint(0x00, 0xff)
    ]
    res = ':'.join(map(lambda x: "%02x" % x, mac))
    return res

def get_windows_version():
    return platform.platform().split("-")[1]
