import json
import base64
from Crypto.Hash import SHA512
from Crypto.PublicKey import ECC
from Crypto.Signature import eddsa
from urllib.request import urlopen

publickey = """-----BEGIN PUBLIC KEY-----
MCowBQYDK2VwAyEAKV1GYFBVMQyEaL1eVQn9fHhs6V+r5JVdRRFd4lx0CpA=
-----END PUBLIC KEY-----"""

signature_url = 'https://IkuoShige.github.io/documentation/main-blog-passencryptcontent-plugin.json'

urls_to_verify = ["https://IkuoShige.github.io/documentation/main-blog-pass./", "https://IkuoShige.github.io/documentation/main-blog-passindex.en/", "https://IkuoShige.github.io/documentation/main-blog-passJetson/", "https://IkuoShige.github.io/documentation/main-blog-passJetson/index.en/", "https://IkuoShige.github.io/documentation/main-blog-passblog/", "https://IkuoShige.github.io/documentation/main-blog-passblog/index.en/", "https://IkuoShige.github.io/documentation/main-blog-passblog/posts/seacret/", "https://IkuoShige.github.io/documentation/main-blog-passblog/posts/tmux.en/", "https://IkuoShige.github.io/documentation/main-blog-passblog/posts/tmux/", "https://IkuoShige.github.io/documentation/main-blog-passblog_private/", "https://IkuoShige.github.io/documentation/main-blog-passblog_private/index.en/", "https://IkuoShige.github.io/documentation/main-blog-passblog_private/2023/09/26/%E9%9D%9E%E5%85%AC%E9%96%8B_private/", "https://IkuoShige.github.io/documentation/main-blog-passblog_private/2023/09/26/tmux-basic-guide/", "https://IkuoShige.github.io/documentation/main-blog-passblog_private/2023/09/26/tmux%E3%81%AE%E5%9F%BA%E6%9C%AC%E3%82%AC%E3%82%A4%E3%83%89/", "https://IkuoShige.github.io/documentation/main-blog-passdocument/fast_lio.en/", "https://IkuoShige.github.io/documentation/main-blog-passdocument/fast_lio/", "https://IkuoShige.github.io/documentation/main-blog-passdocument/jetpack_install.en/", "https://IkuoShige.github.io/documentation/main-blog-passdocument/jetpack_install/", "https://IkuoShige.github.io/documentation/main-blog-passdocument/jetson_clone.en/", "https://IkuoShige.github.io/documentation/main-blog-passdocument/jetson_clone/", "https://IkuoShige.github.io/documentation/main-blog-passdocument/jetson_test/", "https://IkuoShige.github.io/documentation/main-blog-passdocument/livox.en/", "https://IkuoShige.github.io/documentation/main-blog-passdocument/livox/", "https://IkuoShige.github.io/documentation/main-blog-passdocument/mkdocs_colum.en/", "https://IkuoShige.github.io/documentation/main-blog-passdocument/mkdocs_colum/", "https://IkuoShige.github.io/documentation/main-blog-passdocument/sdkmanager.en/", "https://IkuoShige.github.io/documentation/main-blog-passdocument/sdkmanager/", "https://IkuoShige.github.io/documentation/main-blog-passdocument/tmux.en/", "https://IkuoShige.github.io/documentation/main-blog-passdocument/tmux/", "https://IkuoShige.github.io/documentation/main-blog-passdocument/tmux_application.en/", "https://IkuoShige.github.io/documentation/main-blog-passdocument/tmux_application/", "https://IkuoShige.github.io/documentation/main-blog-passdocument/todo_today.en/", "https://IkuoShige.github.io/documentation/main-blog-passdocument/todo_today/", "https://IkuoShige.github.io/documentation/main-blog-passblog_private/archive/2023/", "https://IkuoShige.github.io/documentation/main-blog-passblog_private/category/terminal/", "https://IkuoShige.github.io/documentation/main-blog-passblog_private/category/performance/", "https://IkuoShige.github.io/documentation/main-blog-passassets/javascripts/decrypt-contents.js"]

def __verify_url__(url, signature, verifier):
    h = SHA512.new()
    with urlopen(url) as response:
        h.update(response.read())
    try:
        verifier.verify(h, signature)
        return True
    except ValueError:
        return False

verifier = eddsa.new(ECC.import_key(publickey), 'rfc8032')

print("NOTE: Checking of generated pages while 'mkdocs serve' will fail, because they are modified with the livereload script")

try:
    with urlopen(signature_url) as response:
        signatures = json.loads(response.read())
        for url in urls_to_verify:
            if url not in signatures.keys():
                print(url + ": MISSING!") # signature_url modified or just need to recreate canary script?
            else:
                if __verify_url__(url, base64.b64decode(signatures[url]), verifier):
                    print(url + ": ok")
                else:
                    print(url + ": FAILED!") # file modified!
except:
    print("Couldn't download signatures!")