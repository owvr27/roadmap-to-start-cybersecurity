# Simple example script: prints roadmap steps
roadmap = [
    "Foundations: Networking, OS basics",
    "Programming: Python / JavaScript",
    "Choose path: Red Team or Blue Team",
    "Practical training: CTFs and labs",
    "Build portfolio: GitHub and writeups"
]

def main():
    print("Birds Can't Fly — Cyber Security Roadmap (summary)")
    for i, step in enumerate(roadmap, 1):
        print(f"{i}. {step}")

if __name__ == '__main__':
    main()
