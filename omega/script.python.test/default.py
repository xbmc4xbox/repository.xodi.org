import sys
import ssl
import xbmc

if __name__ == "__main__":
  xbmc.log("Python version: {}".format(sys.version))
  xbmc.log("OpenSSL version: {}".format(ssl.OPENSSL_VERSION))
