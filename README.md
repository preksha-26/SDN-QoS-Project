# Simple QoS Priority Controller using SDN

## 📌 Objective

To demonstrate Quality of Service (QoS) in a Software Defined Network (SDN) by prioritizing traffic and analyzing its impact on network latency and performance.

---

## 🛠 Tools Used

* Mininet (network emulator)
* POX Controller (SDN controller)
* Ubuntu (Virtual Machine)

---

## 🌐 Network Topology

* Single switch topology with 3 hosts:

  * h1, h2, h3
* All hosts connected to one switch (s1)

---

## ⚙️ Steps to Execute

### 1. Start POX Controller

```bash
cd pox
./pox.py forwarding.l2_learning
```

### 2. Start Mininet

(Open a new terminal)

```bash
sudo mn --topo single,3 --controller remote
```

---

## 🧪 Test Scenarios

### 🔹 Test 1: Basic Connectivity

```bash
pingall
```

* All hosts successfully communicate
* 0% packet loss observed

---

### 🔹 Test 2: Normal Network (Low Traffic)

```bash
h1 ping h2
```

* Observed low latency (RTT values are small)

---

### 🔹 Test 3: Congested Network (High Traffic)

```bash
h2 iperf -s &
h3 iperf -c h2 &
h1 ping h2
```

* Increased latency observed
* Due to heavy background traffic

---

### 🔹 Test 4: Throughput Measurement

```bash
h1 iperf -c h2
```

* Measures bandwidth between hosts

---

### 🔹 Test 5: Flow Table Inspection

```bash
dpctl dump-flows
```

* Displays flow rules installed by controller

---

## 📊 Observations

* ICMP (ping) traffic shows low latency under normal conditions
* TCP (iperf) generates heavy traffic and increases delay
* Under congestion, ping latency increases significantly
* Flow rules are dynamically installed by the controller

---

## 📌 QoS Explanation

* ICMP traffic is **latency-sensitive** (high priority)
* TCP traffic is **bandwidth-intensive** (lower priority)
* When congestion is introduced, delay-sensitive traffic is affected
* This demonstrates the importance of QoS in SDN

---

## ✅ Conclusion

This project demonstrates how an SDN controller manages network traffic using flow rules.
By introducing congestion, we observed changes in latency, showing the effect of traffic prioritization and QoS in networks.

---

## 📸 Screenshots

(Add your screenshots here)


---

## 🎯 Key Learning

* Understanding SDN architecture
* Flow rule installation
* Traffic behavior analysis
* Importance of QoS in networks

