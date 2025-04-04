#!/usr/bin/env python3
import os
import sys
import subprocess
import time
import signal
import argparse

def parse_args():
    parser = argparse.ArgumentParser(description='Pornește sistemul expert pentru îngrijirea plantelor')
    parser.add_argument('--backend-only', action='store_true', help='Pornește doar backend-ul')
    parser.add_argument('--frontend-only', action='store_true', help='Pornește doar frontend-ul')
    parser.add_argument('--backend-port', type=int, default=8000, help='Portul pentru backend (implicit: 8000)')
    parser.add_argument('--frontend-port', type=int, default=8501, help='Portul pentru frontend (implicit: 8501)')
    
    return parser.parse_args()

def run_backend(port):
    os.chdir('../backend')
    return subprocess.Popen(
        ['uvicorn', 'app_backend:app', '--host', '0.0.0.0', '--port', str(port), '--reload'],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )

def run_frontend(port, backend_port):
    os.chdir('../frontend')
    os.environ['API_URL'] = f'http://localhost:{backend_port}'
    return subprocess.Popen(
        ['streamlit', 'run', 'app_frontend.py', '--server.port', str(port)],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )

def monitor_output(process, name):
    """Monitorizează și afișează output-ul unui proces."""
    for line in process.stdout:
        print(f"[{name}] {line.strip()}")

def main():
    args = parse_args()
    processes = []
    
    try:
        start_dir = os.getcwd()
        if not args.frontend_only:
            print(f"Pornire backend pe portul {args.backend_port}...")
            os.chdir(start_dir)
            backend_process = run_backend(args.backend_port)
            processes.append(('Backend', backend_process))
            time.sleep(2)
        
        # Porneste frontend-ul
        if not args.backend_only:
            print(f"Pornire frontend pe portul {args.frontend_port}...")
            os.chdir(start_dir)
            frontend_process = run_frontend(args.frontend_port, args.backend_port)
            processes.append(('Frontend', frontend_process))
        
        # Asteapta finalizarea proceselor
        print("\nSistemul expert pentru îngrijirea plantelor rulează!")
        print(f"Backend API: http://localhost:{args.backend_port}")
        print(f"Frontend UI: http://localhost:{args.frontend_port}")
        print("\nApasă CTRL+C pentru a opri sistemul.")
        
        for name, process in processes:
            monitor_output(process, name)
            
    except KeyboardInterrupt:
        print("\nOprire sistem...")
    finally:
        # Opreste toate procesele
        for name, process in processes:
            print(f"Oprire {name}...")
            process.send_signal(signal.SIGINT)
            process.wait()
        
        print("Sistem oprit.")

if __name__ == "__main__":
    main()