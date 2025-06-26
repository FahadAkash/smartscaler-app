from flask import Flask , request 
import time 
import threading



app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the Flask App!"
@app.route('/load')
def load():
    second = int(request.args.get('second', 5))
    thread_count = int(request.args.get('thread_count', 4))
    def burn_cpu():
        end_time = time.time() + second
        while time.time() < end_time:
            x = 0
            for i in range(1000000):
                x += i ** 2
    threads = []
    for _ in range(thread_count):
        t = threading.Thread(target=burn_cpu)
        threads.append(t)
        t.start()
    for t in threads:
        t.join()  
    return f"Simulated high CPU load for {second}s with {thread_count} threads"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)