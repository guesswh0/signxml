import ctypes

# Init
print("Init")
clib = ctypes.CDLL("libkalkancryptwr-64.so", mode=1)
clib.Init()

# LoadKeyStore
print("LoadKeyStore")
storage = 1
password = "Qwerty12".encode("utf-8")
container = "GOSTKNCA.p12".encode("utf-8")
label = "test"
clib.KC_LoadKeyStore(storage, password, len(password), container, len(container), label)
if error := clib.KC_GetLastError() > 0:
    print(hex(error))

# SignXML
print("SignXML")
with open("example/test_xml.txt", mode='rb') as file:
    inData = file.read()
alias = ""
signNodeId = ""
parentSignNode = ""
parentNameSpace = ""
outData = ""
outDataLen = 50000 + len(inData)
res = clib.SignXML(alias, 0, inData, len(inData), outData, outDataLen, signNodeId, parentSignNode, parentNameSpace)
if error := clib.KC_GetLastError() > 0:
    print(hex(error))
print(hex(res))
print(outData)
