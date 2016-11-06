#!/bin/python
import bz2
import base64


def returnLicense():
    licenseText = 'QlpoOTFBWSZTWScWE8UAATN/gHwUBoRQ5//9P///4H///+BgHt6yafVHvaAB9aAABQRXUvJF7UFU\nvrrlCoAn1GjKaAgBUOxkqqAAL1qUqgqIleWosbEAhVarhoCATQTU1NpMJ6U9pQ9BpPUBpoaaabRA\nBoGp6AIISESmeqaDTIDCAZNAAZM1MmgGqfpNMop6mmIGmnqaaGhoyaA9QA0A0AABJpJAhAjU0ajE\njJo9EAaAaDQBoAARKVM0mmgPUmNABNqNMBNMEyZMjCYAQEiEIBNCZE1PSFPTUaeoaNqeoZBoAAZq\nAs3FBAjWJinRQMndocsR87NE1JJelC7STigHrsU5Cbxcgvr83lw7e0ei9i9629jCcMCuZUTE1GMt\nn5/19fx/913/P/27RHuiJ+mHN3H66SNREJml6Dz+qc5SnNdtZw9JEsrss/xalrPKclcXf1rQLAgb\n4YGSzkWf7Xm8rc6tlN6GIpUIj3SS4M8sDtF3SGv2xQEQ9BlLms8X32dXvuUnMNrmomYlWN46Lqmm\n1rNagmq6wsNaVw1UREYoC3oKNYfCJegrIfq3jVpqmnJoWAkYi+yc9DLYevbyB+OY5tLNUoAYP1F1\neHgvX1jgxhPy+N/VHviI+zk91yxHyePXfPdk2pGJDNRkMeCHziOravK9hv/LS1Rxv9e/Rd40PYyX\n0AdxoyiFg7QipXzaqao2e4NIuTLPPTJTyG6B6TKW5CQzOBH4ExkXsEsRhv3OT+FjQ2NHo0KBj1L9\nduPl33rc8TE8zGRI03/StMt0gmdUB3JwtjB0tIi20EBXQgQHw3kQjzUS95LzB/LqYhUAbx0LEaWo\n22ygQGTIyx0XGLWnymOUwh48XQJXaaBzohvs6+3lFcZ77sYB7wfTp1Dp5FRVMUTrErau7dhJnmCy\nyxH2sI22GWaDKQ5DTPPUWGGT4atuM6Z/tnitxtpNCwolApgfydn+iY13SeNXOB00s+IvIGY9TETK\nwDIpYYUcy7IXs445UWjpEGSJd6Fn7LEL6JpV1V3MdJNuHCsERtLBitQjG2CnC/r9xbo8cEyqJSPP\nrzVMgRnbo71KL10iHfxC8PWNHEHCM9vKoS3G6neeHP4cq47ORqh4sFSloMIU+xhXYhwqA9etYV2g\nWbqUXcM0qtlrwEJBwSL76Uo1tzt30N2ROCUrGUbO/OZDZdaZfNYhEujME6ciVwhFqNPsKntu1wfJ\nUe2ngdON5RDMRo7uBmwmqSeU0Vqj6RGmUZRYq0FQRpRSMu+Jis1rHC8EjK2+8o+0PvvPteICXW2X\n00Y7qNFGG0Uj5I49Ytxlwkn3O8oAYsd6iHL9mmHb/txA8hwo72qiPl07upQlfaAt2PhR16SDCiZI\nW/ZUgIYiVFq6UdCsw4m9JMYTPt+HOmjq6GjvdtKGCw+fzyHQtV2LPao25+cNCIg+lAIDZCC3HZdX\n4ZsNu1vbVN7wGD8MwOCjXVzF2Y4hLpmkDv8vPdNRryQcaVmVArQuueTdx5B7bfM7qZOSTvrxorm2\nd1NsFGajaqW0WkEkbi5xMqI2AQgE4mm+rgbu9an22OabEbpBdhOy3RErlloYt10dtx6qHDFfZhna\nI57Tpj0eZcIzqSMe96Dnh87xki0bWWVGZMMxRC7M5wrkPtUUlGwqunyeVH0MGSEYqhAVR5t2L2va\n27ClYpHHdtESaYMfTMMC5c6b0SQGGgcz5+9S5TEZIIl5b0cOzK7QVgiVZYKjKMpHPmMhxR5zYJxv\nLs3vu3CXMBRx0DT5qqx6+N53JyGbJGjGxvRLAQ+FH7DChYQW/urmDapKrDG179n09T1yCoQi38Rs\nenVbqipLkPSVJiG8BIaPsqGZEZEHr1KjojWAYqYaiPG2K48EEE4IdA4V44p5OpfOQjhMuHcLHanQ\n2uAhxiLTAHmO3WpQomeu+BOXfLznjpjSPuG5E5QnGATQNqqp7ynMxBbaoc37FFIqvmqLzGlz8XHp\n/NeCDYlQxwZTKisspFlGQGO1bPdsZlApvXZGwxbc5roHqWnbwqDfAmg1aR33HTq7RVzmYa6EOKy0\nwh3PGzmNMhynIOso261sjDq7nrQPWQN4f371fwJlTnrPBTawk0o87yoxAKUtMOZ2uJiNbz5D6TnO\nuZy2LukI7Rsuig7vQp43cvUEu0E7MP5bVm/JxRfDQq8MmYUCycODPdeNDaSYO11agyRVR75qul6o\nZ3GEILllzllpkLJwOmKRkUOPI38D2mAT4Pd0xvGWHIjPoWg4B66TNS09wiaWfRCEGHpq0EJPp5ZO\nVqHcHoJGYMN4w+EXuXpN2R4DjRVSpHhQkY6xvzypbTeJSqo0R66deIEhJG+F+0DkZViZmqTr1NZs\n49rF5ysIiD2m3Yb19vLLn3P7QAPoZ+hKHCpzhHuMgPnMAt4HnHTyVCJrPp8SHhhdMqns8DFAL5F5\nbbeI9B0d30fLSwVPHWY7V1GzVB5jfx28xtpefWvDibZx8FM2hLqn2bLStLrKzLJd1nueFYBFrMRZ\nidDCrMxJoD9m/qZI/dN5jX3agkUfS6waPEqGxOQoRj61buXM/iEcx6gcu6FGzRQs1C087gOZYG6x\nQr7ZLAb+nGDPXfAonMkUpOO0zKaiopfGqpAGnQgTJAMQl3vuYrOLYTv9so99NnNpvLHsG1iFC/Cw\n+YZGMQmQXuP2ykYMaA+oOQETFXBQEdUqRImGaLEIBwK+ZeS4dGiJhDlthYjZNxw7rVrZCWb5fXwD\noYkQS8aR5xClpDhb1ZOEIb7IAOBHJSL1BQSAD6gqdoKgK6t2IJiQtiKCsC9I1QB+HLRyMkkaTP3E\n1+evSV+ysHBlN7tSBJJvJ+X3iwrppjxHSVDZSMm6Jf6TRXvY29DwM/YZVoP3ni0eKIAVeLajnOC0\n9JuK4bq+F5B2RTRLrsDFLA83wjb3yuWZRemykYYJUQMjuWWgZlKoSLZYGFQyO2uuyXv6/L1Fq0W9\nJgV8RLPdg2qabSWqC0L2Vz/Ule7NEFoWTAo/H06DaqAD6WA4XeTuSdf9oNPS+eXJQfNr6LjvJKy9\njB8w464LgbcJ7nvWo40wXgpCHhTnoBfPMTHOGFjDBhsDjQhSegQWfWyoLPZ29Fh5mD859E+vVPtL\nET7OEHB5U470jZiG0B8NLADGu8bWtkWLEEF855F2lTSCGNS4a1k9SwOtf6obm8U4GNtHwAxV0zPZ\nhCZ6FJGyCy77rkY7Nf8x5Gm2+zJct13PA43LBj3DUh7eXZdmLjvC1OS5n2PsuiWNvOAyXiEUwF+R\nkDSTaLKyQ2vSIGsiCA8oNBesq7iJc5eL5y+Laep3It9BvcMJG5cVVAmPxEdjpM9y0clU5iJLwcmt\ny7Jya1p74uHvnBuxOnnW4nDD0ZET6WFvJggu9R8aElNxT06kRPnT/iiADSGobTr2i055+rDa039E\nWeDDYTm0rTQbfWNTG3z8KSqY9i4DPx6mp8KTctWJtckOlr+Bju4OPBzP0/r00GBzeBctzkvJqz4g\n7EvPiSTtah69zs0aqA/G+BADPy2SoaQifnOYPWqjsVNqJCHT1RlQY8tFCzvmlYviblIlQUencNa/\nf75+bc54Z4IzbKR5tCZwyH6C+db/I/p+AFRcyIzFJJsOt2QGJ2eR95kPQxERFjAsx/iND/jbIZ+l\nO6JWiPnTPj7+1V3kD0Z+RkKhF1KbwtGL5PP8aNTbMOqoP60M0aCvwYGSYG/54BQTaUSwNTMPW576\nq7EcDITTaGhRUhQ9RoHpzweaKRZ9FHy93O0k6Zz94FBmZnSDLBYabBNNJD9PC8W7M14tUEZ6gUrz\npHJuo4d9JG416lTinMANU3a/Jv7hyothSLqzcE9h7KGhdlo2V5GhbJmQwG0XTntD9w8W/WUxNqig\nBjFFhoogkmp5TaQIye7AKSMwvrGYxCMBm5PxxnQZaEiRkqRRBBm6mHVVkgsrIEvfqms6PJ23eF2v\nBrmG2mlqoLVLUOeIdCTI+bnHkysM75i88O3EQ/w8HYXCdMB9qGnyDV+bIVkFFhFeSwk++wxqbbyz\n2ZskXfx5QR8mpS0AUsbFX2sz19S+nPbeTubMsd2oCnp9WYIYhLARJW7JLhQ1lmNEveyTHam8cF2r\naox01WIKQRB1Sxy02sE5KQsPg7d6IVtoLI7CGwOxmYtosl5sI85omkDa8YcBDfY2mlhz50WiVUqW\ntgd2Cly1GtkjSQjKwjDCg/Rgvqwyeoc76nlaHXS/raWV7wFYjBFoJ9njGM72MtWBCEKQF/QV9LgP\nJ2h+zlmEOqlZT6AgU/S9P1Ab60wzjO+3TFJGAyMt1pUDdWkfrujXZ2uyryba2CmuhXDulQM+Gcpa\nJmOlEWkyEIIQdHJc1EriN1voQjy3HngrRWglQqgaPL2HOG7TOyozJGtupHiXkM6hV4j0o5pkSdkb\nIRXUtaKMdkA/xd86e3jRk378562inKTva8+OZqW1VX1ywyVLNeFFggAjJ76US0jFsqKQiL2ytal9\nREeE86bDJxojOmzmcjptEwiOhTxLcyC46J4W0ducpSDxBbBkQUSQ7FBSpIMw6wqYjpMFiLlQW0jl\n6GMZFZVl5RsUs3ovr0GSQMF44voyhR/6H24jRfePhNohNVbBHzSq66wm7d66vhqF2/VTWGUVhDhz\n7vgY+TsJI3ePjKGpWIS8ozzBObcaTZLuGAhJZvpEJHLyo0JR59cZ0bMPJtCscQPWDsX+bG+6Dfra\nszHHnTvN1eS5YwxEvb4+9PPXW+DwcrZebZis+fZNQ8HTf5QWx023QJb3p9X27wFFESunEbtW76mW\nds4YxxfG08Y66mFlwlnSa1t1Brx8puVAxxUzr6Q94XVlnDDo96QsokaiZUXJvPaC1685yjqha4Um\nnsP9vQLGzgnWMLKS4pUoGhfc1t32wuXn0nb+hoW2QbFjBZHG3nE1OmIbPMRP0hBi8I6O9EK7IZlf\n3vV3ezybxqkey4TFkXUfmHx1cD8wjn1TMw4Wi1WzeKLfJS9PhQE/wX9UUfDE2A2dofF+J+biyC+b\nDHE/M4kz12yYMgaRSoVBGLAFgWUQUS+D4naJwyPyT8Sb8oKITeGDIB5ls88L06ZPyM2ZF2Ehzwcy\nAcGph0iybwhNBTrFi8NSob8tZnzhvJJrRPfCXtCAI8Xj5duTQ/OfIFE2QlRZ5K3EKMbbhbmGTCFE\nHbJD5MUFFkiWTpDIT7GCwCKSRQ2tkMYVkAWQMiYk2Uf1qWEjmzgURGGGrJ4+zRDqanLDhigsIKoI\nxYdtg26LJS6A3dKJQRRI1CLJCavWDvkeF3UPP1ZRKQJgujJ02tPjybIP26Pmh69vsA3RYIiiikBE\n2FBoIgzsit/nYyM+N+3PtYK8MynTqpe8ijeJhwiDs7Jk0HNY1QtH93UzYjp95ENBkaJJcCiPkfVx\nyMa9O4Flc2UNMeeYdOg3ZVENUNQM6RA7QiG2j3PkHXbnk1wlow12fcvNFhf4qSWKprrReLKd5b9W\nxmzizMbm5zK1VngsmkTsNa9/o4s9pvH2SfUn3ITk9lEgqkUBjCKIxWKrBQRgpBQiyfGHH0lPAa+J\n8yj89HQiyEQWeGVCMGQ2SxjEwGXWFydrnJKYaUWd/AZ8SkCgRaoTabbOOkICVK9onVJciZtr41BX\nS35jM1D03qG9D6TXhUSlhZg0y27Xyh79cEnsmJKlgfa6+DTzUs2mk0eu9CWP0WoxjaG4YTwcVarH\ngMhV1yvsa05nKTLTCG1obihqyqciVcKW9zg+XXSY7cHjqdk9fTedDbz4zEpJIZMQInbRQF7Fkewz\nYci1RtyViWwPN5dXMGJDdPvGjknbXE1PyZHqzZGmCLqOr7z8uNutNXJuzFoU0bl72NUbekC30Kcm\n2nJphNrSbMXYmIN0xywrJdqaSPr82FT4oC8T6ZyFMNMBZzORTZHqa2Scn0vCGb7nRl50peisDbAp\nk0mx1+WgFdMmsZDJvYPNLLl4DEBtMXLTM6LxAd3SbZUiXtrU1+FpNisumNWmNo2mNXBLShczCVim\nMRkmYXFjhTMt1hDDGqUYLFXTAOE0yJOD/1s5er1Oeox2p1OrkrLJCaZ8nZgkMJoslYS7RZB0aS6d\nRYp9lPG/U7nfnngeuCTeCahpigsgCJNEFFbfgYpTfUGWG4fdHTDdUk/Akmwk+D4dp9+duYcMFAqV\nAr28UPAQjENrBluyjQqTIwKrRhchcMkxkEwMyZNpaamMNIgPM220T0Qk2Z9MnyQFIsDugFfwsqfq\nP30mJF2T7ZjZrejaTDeCzQpiAuMtK0s/TcOg1a3zAPdCLP5+1hYVciMIpIIHRAK4uuXCARUwEQLD\n4+w+uTmhXa6fYGLoN032DW+TZaEPuoSXtxawsQiMFARIRk9ULBFSKcnlQlgRa+OFCR15f1ZwrHp+\n0HFkc7oA0WBgjzPj/GdFdV9u1A87J3mQhxGQp7rxVsfwWU/ElcLQ/aZQYOJowh+2rhWxRYktEHjx\naW7sLPJnkg56qy2ueimOo/hCUhskOuCPSdRe1lFU7bM/hOSAfAn1+MZBZ5HOEOPqgfnEWEFYKqsi\nMk5O6Pp4giIwuncRQYWTWzQu4BFLTX7PXYq65RhSjibTyV/cYX5hkZs+Xv38dB4wZ+NPdrUBU5ML\nkMYV/yWhIcQWfwigLqqBzKDyfxRCdikdpgnpMmUTv37Q/GwN4dPYN2bYAYigLFnYGsh46Q3jPGiH\n3jNSAMBPSlHbKYFsrKNJUkoj3oYmWwFAtGriVdNkxDWVlKFoo1llbQVDEKMIkRBJWmUqxVUGQZOc\novXtKF9qEBn8i4Tk+QH8is7DxlF4UdwBsU8Es3JMZKyViMNMymOYzSQxfmMfyM9885S8sXOhRwyC\nkuhyGcAQgM+hbN9nnEWkjMb0kkLm1KT7CrSsmpcroEhokCbR2aheVdgNpoMPsFYMtIjOeCy+OPnJ\n68k7QkWAiISbnn6hUgiIMVYIqqMUiKxBYU6IUqBww+E448ah56n0HoBvclMtUW5VALcpUwGoolQo\nedjllBQ3y0QHnk+dOK+J/wmhzBFtKKKaBebKXJEKDK95kLTvaJY4iPuL5a3MVK7rxrrMFHNQ7O7v\n1mSddrOWdnn7KGoip2RbSQ1rNSolvDztTyrSSpxq7o1m9UQ0SYdXfFytkJmLDWdGhCTcrSFGYttl\nZiCi2lsyuhnKCAzyy2WOCXdahmZ7KL84c8aKWnysPrgjoHDRzooVHXIg2cnEKKGQiqgGSm9zK3aa\nZrRmOsTTLlmz4fVNkk5+CB2tlrdYKSNKmkzg3031LrBhTVUw0AoGDR+iIzDXzO3Gje/r+dMnb0nd\nhU7GFUqvPoM207+qisHLCHSsNzemMn1tQRx67BN0fbAzLanYmmtK1zB39jxeZ2aekO2OdDQqhAtE\nQI1Zs0EYuFxuF2vRvA3nf6sIHz9JC3JIUItol4JxT3NAKOlSQ5RZlQVVnBdUp3cIPvBlCppUJFwo\nlrSbyjF4iRTCSgNYKggKswJBYgKwRHezL4pRRGhNxPU52KcbuW9tBYbsnZKcaNHFOE5wsjzJ3ILh\nqvDkOme7XdhhPRaRwVIoiFtMDZLERZQQFiyJVZ7visU44jdxii+De+iMYYfXcLK0QmNRvMr4gRkI\nKokeVhrdpFxdmCxZAFh7sKkCoFZJBQFkIsAWQFDXq+jd6LBZbLOdpZxThmJHf3ySaQRFICnrBRqc\njKhtycQPXscCHjacTjrZ0cXnPPbY20lbVt6cUUwqp8NsMFLmGaLMTNsyKXUrRTLRxdWriM7SzjVV\nVYuJ2hUgod1Qh5WwD8CGmSTg6Eo2ZgP3GoBKkSc6sOx7+Ri1cBqeWXK0GnXkUUEfaQDIspHk32hU\ncpJQ0CPo+Hx9QLggYnzYgCHmvys1/+VaI0lOY4O1gNJPjkOi1wtchLkPHmBQ0v5WWCwXmF+DTaSX\nxyvQch02j2LzB65t+7CHriAOMSdkFj5m7qHH7tJVtSSWiV4SCjZ79/dpNmKi6KNKiPlYZjSYMUFK\nUxKD+ZlLfHfCKxlWLK1dL2LJ0yEmMMiZTSd5AEhiBoWMPs2+WQ/KyLArSVloQIs0U1kNB97QloHD\nEHTjc6azTR+SI2f5QqvI9gpwatrMOFUIPhBUF1R2RMvapaEQspgu8BbBgbPe+U2witIhyxskxNPJ\ngqskQ6YU2lBQ5eSAoNJhSyQ9SxUqQwa+WV8QoXXj7es6aN6reszZmaBdmhtJHZpKBhgl22LDLS//\n4u5IpwoSBOLCeKA=\n'
    return bz2.decompress(base64.decodestring(licenseText))

def outputLicense():
    print returnLicense()

if __name__ == "__main__":
    outputLicense()


