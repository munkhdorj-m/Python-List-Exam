import subprocess

tests = [
    "test1",
    "test2",
    "test3",
    "test4",
    "test5",
    "test6"
]

score = 0

for t in tests:
    result = subprocess.run(
        ["pytest", "-q", f"test_assignment.py::{t}"],
        capture_output=True,
        text=True
    )
    
    if result.returncode == 0:
        score += 1

print(f"Score: {score} / {len(tests)}")
