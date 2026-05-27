from log_parser import parse_failed_ips, get_unique_attackers
import tempfile
import os

SAMPLE_LOG = """Jan 15 10:23:01 server sshd[1234]: Failed password for root from 192.168.1.1 port 22 ssh2
Jan 15 10:23:05 server sshd[1235]: Failed password for root from 192.168.1.1 port 22 ssh2
Jan 15 10:24:01 server sshd[1236]: Failed password for root from 10.0.0.5 port 22 ssh2
Jan 15 10:25:00 server sshd[1237]: Accepted password for admin from 10.0.0.9 port 22 ssh2
"""

def create_temp_log() -> str:
    tmp = tempfile.NamedTemporaryFile(mode="w", suffix=".log", delete=False)
    tmp.write(SAMPLE_LOG)
    tmp.close()
    return tmp.name

def test_ip_count_correct():
    path = create_temp_log()
    result = parse_failed_ips(path)
    os.unlink(path)
    assert result["192.168.1.1"] == 2
    assert result["10.0.0.5"] == 1

def test_unique_ips():
    path = create_temp_log()
    result = parse_failed_ips(path)
    unique = get_unique_attackers(result)
    os.unlink(path)
    assert len(unique) == 2

def test_accepted_not_counted():
    path = create_temp_log()
    result = parse_failed_ips(path)
    os.unlink(path)
    assert "10.0.0.9" not in result