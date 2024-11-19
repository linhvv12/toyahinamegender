#region debai
"""
--- ma debai / id
hi(name,gender)

--- nopbai
00 fork tu bainopmau tren replit tu trang web duoiday 
   https://replit.com/@NamG1/toya03hinamegender

01 lam bai vao tep s00_bailam.py, chay Run de co ketqua tatca la 1
02a tao github repo, mo kiemtra tep s00_bailam.py, va lay diachi/url aka githubrepourl

02b dan diachi githubrepourl tu trang web duoiday
    https://forms.gle/yJLsZ5pke3dyq3786

--- debai / problem
Hay viet ham hi(name, gender) xuat ra cau chao theo mota benduoi

--- vidu mau / testcase
Khi chay voi input    | Ketqua output
--------------------- | ------------
hi('Mom', 'f')        | Hi Ms Mom!
hi('Dad', 'm')        | Hi Mr Dad!
hi('TOYA', None)      | Hi TOYA!
hi(None, None)        | Hi!
"""
#endregion debai

#region bailam
def hi(name, gender):
    if not name and not gender: 
        return "Hi!"
    if gender == 'f':  # Nếu gender là 'f'
        return f"Hi Ms {name}!"
    if gender == 'm': 
        return f"Hi Mr {name}!"
    return f"Hi {name}!"
#endregion bailam
