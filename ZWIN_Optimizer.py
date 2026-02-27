#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import subprocess
import time
import getpass
import ctypes
from datetime import datetime

# Cài đặt colorama nếu chưa có
try:
    from colorama import init, Fore, Style
    init(autoreset=True)
except ImportError:
    os.system('pip install colorama')
    from colorama import init, Fore, Style
    init(autoreset=True)

# Màu sắc: nền đen, chữ xanh lá, tiêu đề vàng
GREEN = Fore.GREEN
YELLOW = Fore.YELLOW
WHITE = Fore.WHITE
RESET = Style.RESET_ALL

def is_admin():
    """Kiểm tra quyền Administrator"""
    try:
        return os.getuid() == 0
    except AttributeError:
        return ctypes.windll.shell32.IsUserAnAdmin() != 0

def run_command(cmd, need_admin=False, capture_output=False):
    """Chạy lệnh hệ thống, tự động yêu cầu admin nếu cần"""
    if need_admin and not is_admin():
        print(f"{YELLOW}⚠ Lệnh này cần quyền Administrator! Đang yêu cầu nâng quyền...{RESET}")
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
        sys.exit()
    try:
        if capture_output:
            result = subprocess.run(cmd, shell=True, check=True, capture_output=True, text=True)
            return result.stdout
        else:
            subprocess.run(cmd, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"{YELLOW}⚠ Lỗi khi thực thi: {e}{RESET}")
        return None

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_header():
    current_time = datetime.now().strftime("%H:%M:%S")
    username = getpass.getuser()
    print(f"{YELLOW}Administrator: ZWIN Optimizer 3.0 Ultra - Main Menu{RESET}")
    print(f"{GREEN}WINDOWS OPTIMIZATION TOOLKIT - PROFESSIONAL EDITION{RESET}")
    print(f"{GREEN}Version: 3.0 Ultra | User: {username} | Time: {current_time} | Status: READY{RESET}\n")

def print_menu():
    print(f"{GREEN}MAIN MENU - OPTIMIZATION TOOLKIT\n{RESET}")
    print(f"{GREEN}[ ] BCDEdit Optimization{RESET}")
    print(f"{GREEN}[ ] Services Manager{RESET}")
    print(f"{GREEN}[ ] System Repair Tool{RESET}")
    print(f"{GREEN}[ ] Memory Optimization{RESET}")
    print(f"{GREEN}[ ] Power Plan Configuration{RESET}")
    print(f"{GREEN}[ ] Latency Reduction{RESET}")
    print(f"{GREEN}[ ] System Cleaner & Disk Cleanup{RESET}\n")
    print(f"{GREEN}[ A ] About{RESET}")
    print(f"{GREEN}[ R ] Auto Run{RESET}")
    print(f"{GREEN}[ X ] Exit Program{RESET}")

# ====================== CÁC CHỨC NĂNG CHÍNH ======================

def bcdedit_opt():
    print(f"{GREEN}▶ Đang tối ưu BCD (Boot Configuration Data)...{RESET}")
    run_command('bcdedit /set {default} bootmenupolicy legacy', need_admin=True)
    run_command('bcdedit /set {default} bootux disabled', need_admin=True)
    run_command('bcdedit /set {default} quietboot yes', need_admin=True)
    run_command('bcdedit /timeout 0', need_admin=True)
    run_command('bcdedit /set {default} useplatformclock false', need_admin=True)
    run_command('bcdedit /set {default} tscsyncpolicy enhanced', need_admin=True)
    print(f"{GREEN}✅ Hoàn tất BCD Optimization!{RESET}\n")
    input("Nhấn Enter để tiếp tục...")

def services_manager():
    print(f"{GREEN}▶ Đang tắt các dịch vụ không cần thiết cho game...{RESET}")
    services = [
        'SysMain', 'WSearch', 'DiagTrack', 'dmwappushservice',
        'XblAuthManager', 'XblGameSave', 'XboxNetApiSvc', 'wuauserv'
    ]
    for svc in services:
        run_command(f'sc stop {svc} >nul 2>&1', need_admin=True)
        run_command(f'sc config {svc} start=disabled >nul 2>&1', need_admin=True)
        print(f"  • {svc}: đã tắt")
    print(f"{GREEN}✅ Hoàn tất Services Manager!{RESET}\n")
    input("Nhấn Enter để tiếp tục...")

def system_repair():
    print(f"{GREEN}▶ Đang chạy System File Checker (SFC)...{RESET}")
    run_command('sfc /scannow', need_admin=True)
    print(f"\n{GREEN}▶ Đang chạy DISM để sửa ảnh hệ thống...{RESET}")
    run_command('DISM /Online /Cleanup-Image /RestoreHealth', need_admin=True)
    print(f"{GREEN}✅ Hoàn tất System Repair!{RESET}\n")
    input("Nhấn Enter để tiếp tục...")

def memory_optimization():
    print(f"{GREEN}▶ Đang giải phóng RAM và dọn cache...{RESET}")
    run_command('ipconfig /flushdns', need_admin=False)
    run_command('rundll32.exe advapi32.dll,ProcessIdleTasks', need_admin=False)
    run_command('del /q /f /s %temp%\\* >nul 2>&1', need_admin=False)
    run_command('rd /s /q %temp% 2>nul', need_admin=False)
    run_command('mkdir %temp% >nul 2>&1', need_admin=False)
    # Đóng các tiến trình không cần
    progs = ['OneDrive.exe', 'Teams.exe', 'Skype.exe', 'Spotify.exe']
    for prog in progs:
        run_command(f'taskkill /f /im {prog} >nul 2>&1', need_admin=False)
    print(f"{GREEN}✅ Hoàn tất Memory Optimization!{RESET}\n")
    input("Nhấn Enter để tiếp tục...")

def power_plan():
    print(f"{GREEN}▶ Đang kích hoạt Power Plan High Performance...{RESET}")
    run_command('powercfg /setactive 8c5e7fda-e8bf-4a96-9a85-a6e23a8c635c', need_admin=True)
    run_command('powercfg -change -monitor-timeout-ac 0', need_admin=True)
    run_command('powercfg -change -standby-timeout-ac 0', need_admin=True)
    run_command('powercfg -change -hibernate-timeout-ac 0', need_admin=True)
    run_command('powercfg -change -disk-timeout-ac 0', need_admin=True)
    print(f"{GREEN}✅ Hoàn tất Power Plan Configuration!{RESET}\n")
    input("Nhấn Enter để tiếp tục...")

def latency_reduction():
    print(f"{GREEN}▶ Đang tối ưu độ trễ hệ thống (Latency Reduction)...{RESET}")
    # Tăng priority cho game, tối ưu network, v.v.
    run_command('bcdedit /set disabledynamictick yes', need_admin=True)
    run_command('bcdedit /set useplatformtick yes', need_admin=True)
    # Tối ưu TCP/IP
    run_command('netsh int tcp set global autotuninglevel=normal', need_admin=True)
    run_command('netsh int tcp set global rss=enabled', need_admin=True)
    run_command('netsh int tcp set global chimney=enabled', need_admin=True)
    # Tạo báo cáo độ trễ (không bắt buộc)
    run_command('powercfg -energy -output %USERPROFILE%\\Desktop\\energy_report.html', need_admin=True)
    print(f"{GREEN}✅ Hoàn tất Latency Reduction! Báo cáo năng lượng đã lưu trên Desktop.{RESET}\n")
    input("Nhấn Enter để tiếp tục...")

def system_cleaner():
    print(f"{GREEN}▶ Đang dọn dẹp hệ thống...{RESET}")
    run_command('cleanmgr /sagerun:1', need_admin=True)  # Chạy dọn ổ C với cấu hình mặc định
    run_command('del /q /f /s C:\\Windows\\Prefetch\\* >nul 2>&1', need_admin=True)
    run_command('del /q /f /s C:\\Windows\\Temp\\* >nul 2>&1', need_admin=True)
    print(f"{GREEN}✅ Hoàn tất System Cleaner!{RESET}\n")
    input("Nhấn Enter để tiếp tục...")

def about():
    print(f"{YELLOW}ZWIN Optimizer 3.0 Ultra - Professional Edition{RESET}")
    print(f"{GREEN}Công cụ tối ưu Windows chuyên sâu cho game thủ.{RESET}")
    print(f"{GREEN}Phiên bản: 3.0 Ultra{RESET}")
    print(f"{GREEN}Tác giả: Admin{RESET}")
    print(f"{GREEN}Liên hệ: support@zwin.com{RESET}\n")
    input("Nhấn Enter để tiếp tục...")

def auto_run():
    print(f"{YELLOW}▶ BẮT ĐẦU AUTO RUN (chạy lần lượt tất cả chức năng){RESET}\n")
    funcs = [
        ("BCDEdit Optimization", bcdedit_opt),
        ("Services Manager", services_manager),
        ("System Repair Tool", system_repair),
        ("Memory Optimization", memory_optimization),
        ("Power Plan Configuration", power_plan),
        ("Latency Reduction", latency_reduction),
        ("System Cleaner & Disk Cleanup", system_cleaner)
    ]
    for name, func in funcs:
        print(f"{GREEN}>>> Đang xử lý: {name} <<<{RESET}")
        func()
        time.sleep(1)
    print(f"{YELLOW}✅ AUTO RUN HOÀN TẤT!{RESET}\n")
    input("Nhấn Enter để tiếp tục...")

# ====================== MAIN ======================

def main():
    if not is_admin():
        print(f"{YELLOW}⚠ Tool cần quyền Administrator để hoạt động đầy đủ!{RESET}")
        time.sleep(2)
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
        sys.exit()

    while True:
        clear_screen()
        print_header()
        print_menu()
        choice = input(f"\n{GREEN}Nhập lựa chọn của bạn (1-7, A, R, X): {RESET}").strip().upper()

        if choice == '1':
            bcdedit_opt()
        elif choice == '2':
            services_manager()
        elif choice == '3':
            system_repair()
        elif choice == '4':
            memory_optimization()
        elif choice == '5':
            power_plan()
        elif choice == '6':
            latency_reduction()
        elif choice == '7':
            system_cleaner()
        elif choice == 'A':
            about()
        elif choice == 'R':
            auto_run()
        elif choice == 'X':
            print(f"{GREEN}Tạm biệt!{RESET}")
            break
        else:
            print(f"{YELLOW}Lựa chọn không hợp lệ! Vui lòng nhập lại.{RESET}")
            time.sleep(1)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{GREEN}Tạm biệt!{RESET}")
        sys.exit(0)