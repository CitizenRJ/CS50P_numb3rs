from numb3rs import validate

def main():
    test_ip_true()
    test_ip_false()

def test_ip_true():
    assert validate("111.112.113.114") == True
    assert validate("11.12.13.4") == True

def test_ip_false():
    assert validate("1234.112.113.114") == False
    assert validate("1.333.444.555") == False
    assert validate("RJ") == False

if __name__ == "__main__":
    main()
