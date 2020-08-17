import time

import prettytable as pt

balance = 1000

acount_log = []


class Bank:
    def __init__(self):
        """初始化"""
        global balance
        self.balance = balance
        self.acount_log = acount_log

    def deposit(self):
        """存款"""
        amount = float(input('请输入存款金额: '))
        self.balance += amount
        self.write_log(amount, '转入')

    def withdrawl(self):
        """取款"""
        amount = float(input('请输入取款金额 '))
        if amount > self.balance:
            print('余额不足')
        else:
            self.balance -= amount
            self.write_log(amount, '消费')

    def print_log(self):
        """打印交易日志"""
        tb = pt.PrettyTable()
        tb.field_names = ["交易日期", "摘要", "金额", "币种", "余额"]
        for info in self.acount_log:
            if info[1] == '转入':
                amount = '+{}'.format(info[2])
            else:
                amount = '-{}'.format(info[2])
            tb.add_row([info[0], info[1], amount, '人民币', info[3]])
        print(tb)

    def write_log(self, amount, handle):
        """写入日志"""
        create_time = time.strftime('%Y-%m-%d%H:%M:%S',
                                    time.localtime(time.time()))
        data = [create_time, handle, amount, self.balance]
        self.acount_log.append(data)


def show_menu():
    """显示菜单"""
    menu = '''菜单
    0: 退出
    1: 存款
    2: 取款
    3: 打印交易详情
    '''

    print(menu)


if __name__ == "__main__":
    show_menu()
    num = float(input('请根据菜单输入操作编号: '))
    bank = Bank()
    while num != 0:
        if num == 1:
            bank.deposit()
        elif num == 2:
            bank.withdrawl()
        elif num == 3:
            bank.print_log()
        else:
            print('您输入有误！')
        num = float(input('请根据菜单输入操作编号: '))
    print('您已退出系统')
