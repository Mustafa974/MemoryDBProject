
class Headers(object):


    def __init__(self):
        """
        定义公有成员cookie列表
        """
        self.cookies = [

            'csm-sid=847-5093621-8422399; x-amz-captcha-1=1541363621290470; x-amz-captcha-2=QSIhH7eB40K6UxukWhxjSw==; skin=noskin; session-id=131-4386163-7335614; session-id-time=2082787201l; ubid-main=132-7215837-4167420; x-wl-uid=1jl1Dqqnsf3fPfm+X7875yINqcCjMdtuVr4JdeeIJSazrLiGoG0f4Pevl/DRdX4s9MjOTp50GpS8=; session-token=se+mnbeDBStFkPOuhsxBxWBy/7d8v/drCoyo1E7mFvoudQ0/8poYk/r+VILKcqIAEQEtu4QBX5lOZKiwBeYvtMD2fJimJC7kx/1kXErH4Th2t6EIr8VnenYYaRCsTfVXCUVaIG2fYrPQxhvDTZ27P1JdRu8hE95JRJE4m4yKO5wBAKr5XbxyK06JYziO/lUKEAp0WmV83Dadt9k/JhyYddxMwp2rIk0ZdIzfAtA57BQMpnEU2q+Am4i2xsgGTxVN; csm-hit=tb:s-NN6391Z7SQ7TDGWMSV03|1541356422499&adb:adblk_no',
            'csm-sid=525-5868100-1610889; x-amz-captcha-1=1541363659730705; x-amz-captcha-2=5CGDIv7kegv+C+dOc8EBIA==; skin=noskin; session-id=134-8440450-8046340; session-id-time=2082787201l; ubid-main=134-1770123-8116406; x-wl-uid=19sCVtkwGZJndhAHLchajEUtkO6vt9Mtj5HJxEH12eKxsXEToUikKRJ8aNHdvsI/d7AupBlXwoEQ=; session-token=ZKRV84JT798vCxd1AJ+bDsjudgg+5DCtOdnbWuSPprMnCqI/gwpKqkSDLpvWz2sYrjK8gxjhbhSNzj2KxJnltCzeImfaUNeR52KdLsAXjw55re4wVGCregVuxTm3pn4ct7vlesfh3WY417dn6yhKHIvLwi7NRrBGaVuYF7WUfhRmuuQ9YnKscfmHi/duFoFKx1v1K2qsc5gpAp49nZe723ID1jD3VsCqIZHUH1ZesCWi0nhDRv9Xm6SQKQ86yy1c; csm-hit=tb:s-JJ71R567H9FHAP42HDRR|1541356460769&t:1541356464140&adb:adblk_no',
            'csm-sid=401-2496332-4049050; x-amz-captcha-1=1541363692460644; x-amz-captcha-2=W1TuUchvwXEjpR3F4ZkQ3g==; skin=noskin; session-id=140-5001857-4904964; session-id-time=2082787201l; ubid-main=132-7974469-3985465; x-wl-uid=1eOyuh0z3EfjLkSxz0cs5TKol3QL6s4SnHYV8nn96A6wym3HTVe0ema5OYSsS/HhBl9+S7sSiaNk=; csm-hit=tb:s-47G1EKX3WCENKCW6XN29|1541356493822&adb:adblk_no; session-token=B4Uc5sfvP9euHbddSW22kCEQLVsIFlf75wABILNtUim/RNx6e/4DhcpUu/kFBnqX/p6bVTQLg88xCqUn9CKy48jchrO/CM2TOQcdPDxmARgAIeYa5d695WQks9c/MDZr54S/hojf7Brn03cqg2T7M48uBwPx/ML9lxl8AkHdehvmaOEI+aDehEshF/5s21QM7aU9n/0BzVnyMQQwByF0GULf2IZLUrygp46FrgKztD6WNg7i/vPJpflahkCEPL8+',
            'csm-sid=212-3466806-2433908; x-amz-captcha-1=1541363723641063; x-amz-captcha-2=97rdyrE3p32A4JFj32fSvQ==; skin=noskin; session-id=134-1332869-7774167; session-id-time=2082787201l; ubid-main=132-6437484-1475013; session-token=Qi8u0LFGXiCddyh6UkQDKpWGsGt+omEck2mCOpG6WLDyRlNECfbZbCq8BdEHJu0mXDUmj+uBaGA36S9zr0WuCUpyhiekOJ2DyIOYN+A/bHm6loKsd66fOcO+RBHGVFmXLOU210DhpgApxaIDneglFhXdw+N1VzuVE3eVGpdm3RwLVy1pVHtm4m+wcn96Yaw4ktKtunYI1sTgNKbWHiBJHbyzU9lKQzO4ZAjVLM7t5gbIDOL9Y40GMH43xsedZH3K; x-wl-uid=1gFss+b6KZ8X3tT+AKSF1y2fV8L7M5R4nyOXAlMnME80Uq1MJOC8Obnk1Qhd0leZmhcTGw0duhFQ=; csm-hit=tb:s-G72E0XTD27G7WTS9TZ9Z|1541356524627&adb:adblk_no',

            'csm-sid=895-7723151-6636066; x-amz-captcha-1=1541363764386565; x-amz-captcha-2=Rbrk2wpr4+y7sL5YKnrqzg==; skin=noskin; session-id=140-8188281-5529002; session-id-time=2082787201l; ubid-main=132-1340286-2340431; x-wl-uid=1QCb2gHGropUNuPUeQru7pW2CKKVI1il31qMYh7Fu+C/EqPqqUpAY8I4fpBXqk1NfDhb1Yd9fWSE=; csm-hit=tb:s-PREK3RP8TY79J4WY3VF7|1541356565999&t:1541356570095&adb:adblk_no; session-token="XNhK1jfY61i8Hdr6xBjYk0q3JXpYqDzb3vRyXNGU5XDqRU4KjxcCGffs4W0qPrfPHmsj9F+yz5M+lwtpEae9UkoBxRkjmg87EpHgLlQkcc9sFIL83UDnsWihQJxDGyNN5qZ/yCvsl6dZPkdtvSRljLfVyFesHx0HW/oefaEq7Eb07xLDHgjDRntiPAH1Q1NsI8L0fjZWqlSO4BdN4H126SBkRSR697iAWletRUDX6E8ixOUJfE7NIAsBkra7nVHVSdLzIAXVLas="',
            'csm-sid=988-4094104-8483190; x-amz-captcha-1=1541363794066783; x-amz-captcha-2=8vOZO131kZ8gf8ZLezRw7A==; skin=noskin; session-id=147-8513879-2176315; session-id-time=2082787201l; ubid-main=135-0134697-0636622; x-wl-uid=1TStFKRvSCdy+3Wj9zgI4FSvO3JEaTWG0+awczSUWVNuPgO5DpmLLxhiQegxuME3JTHTaey/W28Y=; session-token=rDYLp1EOoIMG0VvKyIf0G0K9BDQPYdgyOZ0UfOrbAKP1cPI449ks2E353q9hRnDtLBHKNXK6VVkaG5zuIHiL/8jzKz+Qug1O/B/gV8mvye6t2Dv1z8NN6CcMPAsCDkiKAhU4js+p9o1Ee+i7mS1my+f8iXFMr+nv/flNsCXUZTwJkmnjVZj8H9ciMEPinFU/w99banDEG47Q/zKGY4pvoxv89voMWzIkaRze+8Bg17e6CCqiT1u8MHRI7kuHDFx/iorUW9hgGqw=; csm-hit=tb:s-TN16HS599JA91905D2DM|1541356595079&t:1541356597903&adb:adblk_no',
            'csm-sid=291-0338533-6560171; x-amz-captcha-1=1541363823754280; x-amz-captcha-2=viBTUJFskC9a1cpdk0fATg==; skin=noskin; session-id=134-2261915-1675402; session-id-time=2082787201l; ubid-main=135-7761177-7123116; x-wl-uid=1Ov7BxWRITctQxyqDu5dEBdg2FfkNXB1rrdw//rrgzN7WMlrNjthJrraw8YKqtznSXqp99axxzfI=; csm-hit=tb:s-PBP44WHQYMSWM66SJKJK|1541356625097&adb:adblk_no; session-token="rGND9HiqKpzcrlezPoByyWiSV6dZQtIfh8zRv5wMzJhkCzdhKqwvhShorI/4vemX4kT6U8MGp1hAsqs2zt+iAdGWfniCuMOctqiw+p3n2GO7aYHw4Yxr+tE2HxElwWI0yb15nSZma/JroEwBgnTy8REUQSIecSX9sdHyrzlxUSYHGANl+0yYPTC7cQnjUlJmMcgEueLBdtUkqGqhI09FePXrM6znSkspT/rCfYhcRh/7njyazdj2qxFMUe2cD2dHxYm1XVy4fdU="',
            'csm-sid=349-0831873-1895140; x-amz-captcha-1=1541363859509582; x-amz-captcha-2=WlEvWdsefwwi+ypsRc3Row==; skin=noskin; session-id=136-2974453-6800643; session-id-time=2082787201l; ubid-main=132-7145560-5566525; x-wl-uid=1QUHzxQUKU0LGrg2EEVCei2uWkhXJpBiEQ5FyKbQbWC0CtQFdBJzqzyAmmqUJ/Ze+UPCD11o40wo=; session-token=l4/yJHwHBBlAaxPSENVlc81mjgwrLBbQnlaEYuxFbqz8iQSDcvhHIjH3C8X8URcOTjP4tjLZ1wT1/dkfSXHiV4lXFjkldOzEu9xl3C5et52uOOOOSJ8ys/yw/HFmmhq4mLw3QXThD/3OCoMumoiW8XjHUwdTuNuBE9TQaces6xIxf09AulDxN/z1N9H0VDI+MEzwMgKH977iX2vRar4syzXWXu47vsAEau/KjKhlrmJTWCulcoKX1SEiRU401VVy; csm-hit=tb:s-44JXVPP94CGRA2PHX0NX|1541356660679&t:1541356665016&adb:adblk_no',

            'csm-sid=857-3159757-5307984; x-amz-captcha-1=1541363887495971; x-amz-captcha-2=+d0Py+PaJZMNzNrnJz22oQ==; skin=noskin; session-id=147-2046843-0929329; session-id-time=2082787201l; ubid-main=133-7382169-0831850; x-wl-uid=1Qi6+12JktxvyJ7WstGBBpekKnNjf0fqHQGAt47qKsKVRWkprKAkSbQxJKoaQVpctNBVO3bXyarw=; csm-hit=tb:s-FJH75MZ6KT03MFZBMWVD|1541356688652&adb:adblk_no; session-token="VNmNGWgJmGTkErUFNplAPz8R6bWJ7CLMviItf6xAlkkhea6bz0K8ZqJNhdBF99smxMvsE+96LlK++j00tKge1cbDh54bdqjyfVY4BnWDIxkTeyv4uyDtlQegJ+S+3BYaTBRlhsSRDOO5wrGdttT+eCHqTGUulqYzT5oZDlAMr7j/mM2VWu/ItA1DndV462nUEpP0MF0a/WKpZpWEPeZGCAFPxBNtgqpg9m/uMW3ArJLHqjNT6VzYn9h/clpNXbPpFAcKCNMIteg="',
            'csm-sid=599-2584226-4906762; x-amz-captcha-1=1541363914327906; x-amz-captcha-2=nWYN9ZMwXV+aGywOoIxFrQ==; skin=noskin; session-id=142-8740089-0598844; session-id-time=2082787201l; ubid-main=133-5728931-2563032; x-wl-uid=1DIEp6F+GS0ZPuxX79emO7K3ia2UDamGmGmf/7+kWoiWzCzrzu9ME0+Uquf7mQj5/zku+4/bKuIw=; session-token=0pni8pWN81uzqrsn4OMu4sfLHJC9P2dVndpnWdnUQHM1igdzyUfhonwcz3gEHDva0qMAvoS4vXFO7R5DRkOnK8Cxb79jveZx8qG6pjnLGKH6gMWucfleb9kh/TXLg4GGu31TB9Bk6xCVJhyp+P9xLUVrYTRCtknA2q3wVv6J9WkjdfFcDGO5Zjr6nvXOsKGc5K9cOU4A7vL4PUhj0J6QWLZdnxs20yzsafkSIPlnNGKep9+xppU8N9aVaRq/wJBp; csm-hit=tb:s-RC17Y4XJNNFN0DA7X93Y|1541356715401&t:1541356718490&adb:adblk_no',
            'csm-sid=362-1074980-7595916; x-amz-captcha-1=1541363943817959; x-amz-captcha-2=JUytIwN//FV73rPDiSB9Ww==; skin=noskin; session-id=142-3496982-9948822; session-id-time=2082787201l; csm-hit=tb:s-7SEH739SB19R052ZV9PS|1541356745332; ubid-main=135-1904910-3591364; x-wl-uid=1uRx1G2hwiD7q50imjueHiFKrVjrDS9Ox3dqIwMVFiOlo1c6WnfOb0V2iEpf0WSjo8uja2m13RH4=; session-token="T00p+66V0WXS1+pjOGn3UHadG6lhdb63hf3d/imzrrnhQXvUj/T1c9jRqFEC6Qy1oRYpm9xEEWujOZ8kkpwix2/1alrOsTwd6YF+TbntjumqhZCCm7lryCPNQXGCR+31yj9rY1wwAEg+0NYGDQfoHWYMlvVnNqFTU9OwOPnugXDYde+QVsJpb9/HqFaKRo9UEYF+8BhmRuCHlclJIfxG8BODkrk4znMHlxWGwZQuc2buzgnF6wb6i2y1HCmfGhDL9/qPMZ8CDQo="',
            'csm-sid=297-1453158-9703505; x-amz-captcha-1=1541363988815607; x-amz-captcha-2=XOLGXfUa/aSsjXxkBfWcRA==; skin=noskin; session-id=140-9742039-1937908; session-id-time=2082787201l; ubid-main=130-2257505-5921544; x-wl-uid=1ujDt8DPtOeGyqOFJMEQroJCvQc/1s7N378UFgW5gcQgCkm68QPDJyqO8Hjs7XZPSqbPjY89NdGs=; session-token=vAGWGPFsr6iCsv4ux/xnwZX/EyWYuIb1hXQ8vyzofXWgZbcADhA8qXKksVCEXctZrUDGXnCYCXjm7wF+19vp6OCPp5BStG0fbn3siM8O2wO7bxTdEUAY1YGsEzsN+0UWfKIuTj8th7oBOta5HSFrEWwV8wKQa7U8Ea8TKguH0F99Zbz5nsTKCdMj+MqV8LF79NEYNzn/TQuexusDp3IKUxQR8RIy13xoaCVkcnPfXReWb21OnwzftOC02GP7JDRQ; csm-hit=tb:s-XZE8YCSH1M6J9F0ZGMV1|1541356789530&adb:adblk_no',

            'csm-sid=371-5162640-1516075; x-amz-captcha-1=1541364014572099; x-amz-captcha-2=S+QkW2SvslrenrvduTJ/4A==; skin=noskin; session-id=132-3628518-0914049; session-id-time=2082787201l; csm-hit=tb:s-52JDBNFNGV55818HQ05Z|1541356815432&t:1541356815432; ubid-main=131-0237677-1762969; x-wl-uid=14WXotAbNNsBqU39pVNEU1VW3IXqazBlbvKy1SysGDPSFSbIIIly1J8K8XITZtL/sZA3eilzR5dM=; session-token=I+jVuFacf3y19DozmMQJ7kt4HJ1aUdp8Jqr+2ejGqEsUVwN4UAqdfThiqT/LnvSKN0uiqcfs5a3t4C4CbyXZPDC2ZEXjYXwrn6gIVhSlrR/1lRFUjUBj2LMQAP5dDbx3EVfEiZ5S4xDAMxpS+tpd0ZO7EIQi4SFdGPaiQ/LjJ2H9/vd1k5TzhUVOA3ABtPT+a/Krv6DahwRTudhRD2Y0rQeQkIw/U3RqXE5ZyTcPdL/kmg641T1iUhJQthdZjT4j',
            'csm-sid=346-4425591-1962541; x-amz-captcha-1=1541364048300097; x-amz-captcha-2=vjuY4KWjCzw7+5NTiAdBDQ==; skin=noskin; session-id=132-2837731-3334934; session-id-time=2082787201l; ubid-main=135-1888697-5650919; x-wl-uid=13lujx23jDIDlEUfa34un+M3Dp/Rj0N4ii5WpkXCVd6VzuA8IxM1BU5yFuP/TwabinTaxpz07LAI=; session-token=dCUQ1eq3FIWEH0EFvJDHGreTmdrl00obb/PvvkdSi36fdhOrqlh6iSxQKE9zZ35lmVTpXAchFCol6VAxNdQDnpx06RLEV0HrxjJgwKUrKv7y932WXZKvaBXpFj0aH/Vdh5efooyW8tBrYp50FFwnPHKujUYIL8sgnhyCzerjeEgA7hV6CS0AWiDFl/20W97tgrEgZqMQLeLzUHqaned/yxcM9zLEezDmBHd/cn6uQghuwvAxxIS12XLnYmtMK+yf+bibw+X75WQ=; csm-hit=tb:s-GP3W72GC00P4VBD9NJ0A|1541356849299&t:1541356852254&adb:adblk_no',
            'csm-sid=719-9667586-9056058; x-amz-captcha-1=1541364075541323; x-amz-captcha-2=krrsAPk6g7ytAVW6Y76pew==; skin=noskin; session-id=146-2847803-5851008; session-id-time=2082787201l; ubid-main=130-7086180-7906854; x-wl-uid=14Ubt9ueHV6mvGX32eTR1FLF0X6NInscu2MbyXcXMRyO+PWzX8nfImgOKf2PzFnUnxuS6vJQn9CU=; csm-hit=tb:s-G5RQYEMRJ4M6NNJS29NZ|1541356878065&adb:adblk_no; session-token=xuEd04M39MVFwmnW8+guhjukLnbljLS2veOYWHAaBMGoir9Qq8Ath1fDpPdqKozaDcIuR7oK2JWrPTfYtLYd3Y+yf0lYlf1WieDmljhJb7sfrVM2XLShdW3kizmjAV65Ez033aaq2u0N94qsbbO81odOWBcjYfUVd8hZo/P9dcLkN/HfS2dBUUByenqkFRrU',
            'csm-sid=410-0785735-7011909; x-amz-captcha-1=1541364112881476; x-amz-captcha-2=XZm1bP7kfNI/xo7g9PyGSA==; skin=noskin; session-id=147-3889687-6666761; session-id-time=2082787201l; ubid-main=132-9631976-5573151; x-wl-uid=1XvUni8WwNCKOo2EhAokStXK2fWRB1/fFopwC3Z5KBZZjQdtdXji+mP8hMWaQWWzT4EZ+md0AhGk=; session-token=1Tu4UiVUe3ud7KwUtmhCq38cR1NXX+JqLFCHRSb/MrTwpEwczRQ/1xHMGQmaHSXuqv+LBb9YmQGc4oaC4LMyfVkPVKzuUgr2PfulSaJXJYttCt+PBWRhgHucmRxSSx3IHUorNQfj23FCTXUkelDo+rjSh035XqwKrohi/CgwlIN0mvBC5wHBZhQWWoZyTQl+RtywL3tl0/YRu6GOAjDpexJOTWL7E9a8GtrGqvY9CNZTsjxX+nrnrzTzo3yzyjge; csm-hit=tb:s-TDC41BZG6FH5QAZKXWFB|1541356914118&adb:adblk_no'

        ]


    def get_headers(self, tag):
        """
        获取一个headers
        :param tag:
        :return:
        """
        headers = {
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'zh-CN,zh;q=0.9',
            'cache-control': 'max-age=0',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
            'cookie': self.cookies[tag]
        }
        return headers

