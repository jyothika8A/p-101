import random
response = "y"
while response == "y" :
    ram = random.randint(1,6)
    if ram == 1:
        print("[-----]")
        print("[     ]")
        print("[  0  ]")
        print("[     ]")
        print("[-----]")

    if ram == 2:
        print("[-----]")
        print("[0    ]")
        print("[     ]")
        print("[    0]")
        print("[-----]")

    if ram == 3:
        print("[-------]")
        print("[       ]")
        print("[ 0 0 0 ]")
        print("[       ]")
        print("[-------]")

    if ram == 4:
        print("[--------]")
        print("[  0   0 ]")
        print("[        ]")
        print("[  0   0 ]")
        print("[--------]")

    if ram == 5:
        print("[---------]")
        print("[  0   0  ]")
        print("[    0    ]")
        print("[  0   0  ]")
        print("[---------]")

    if ram == 6:
        print("[----------]")
        print("[  0  0  0 ]")
        print("[          ]")
        print("[  0  0  0 ]")
        print("[----------]")

    response = input("press y to continue and n to exit")
    print("\n")

        