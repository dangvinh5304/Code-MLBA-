from salesmanagement.libs.connector import MySQLconnector
from salesmanagement.models.nhanvien import NhanVien

class Nhanvienconnector(MySQLconnector):
    def DangNhap(self, username, password):
        cursor = self.conn.cursor()
        sql = 'select * from nhanvien where username = %s and password = %s '
        val = (username, password)
        cursor.execute(sql, val)
        dataset = cursor.fetchone()
        nv = None
        if dataset != None:
            id, manhanvien, tennhanvien, username, password, isdelete = dataset
            nv = NhanVien(id, manhanvien, tennhanvien, username, password, isdelete)
        cursor.close()
        return nv
