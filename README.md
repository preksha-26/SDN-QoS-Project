# Simple QoS Priority Controller using SDN

##  Project Overview

This project demonstrates **Quality of Service (QoS)** using **Software Defined Networking (SDN)**.
A POX controller is used to install **priority-based flow rules** in a Mininet network so that certain traffic is treated as more important than others.

---

##  Objective

* Prioritize selected network traffic using SDN
* Implement QoS using OpenFlow rules
* Analyze how priority affects packet forwarding

---

##  Key Concept

In this project:

* Traffic from **h1 → h3** is given **high priority**
* Traffic from **h2 → h3** is given **low priority**

This is achieved by assigning different **flow rule priorities** in the switch.

---

##  Network Topology

```
h1 ----\
        \
h2 ----- s1 ----- h3
        /
   POX Controller
```

* **h1, h2** → Clients
* **h3** → Server
* **s1** → OpenFlow switch
* **POX** → SDN Controller

---

##  Technologies Used

* **Mininet** – Network emulation
* **POX Controller** – SDN control logic
* **OpenFlow Protocol** – Controller-switch communication
* **Python** – Controller implementation

---

##  How It Works

### 1. Controller Initialization

* POX controller starts and waits for switch connection

### 2. Switch Connection

* Mininet switch connects to POX
* `ConnectionUp` event is triggered

### 3. Flow Rule Installation

Controller installs 4 flow rules:

| Flow    | Description           | Priority |
| ------- | --------------------- | -------- |
| h1 → h3 | High priority traffic | 100      |
| h2 → h3 | Low priority traffic  | 10       |
| h3 → h1 | Return traffic        | 100      |
| h3 → h2 | Return traffic        | 10       |

---

## Flow Table Example

```
priority=100,in_port=1 actions=output:3
priority=10,in_port=2 actions=output:3
```

---

##  Execution Steps

### Step 1: Start POX Controller

```bash
cd ~/pox
python3 pox.py misc.qos_controller
```

---

### Step 2: Start Mininet

```bash
sudo mn -c
sudo mn --topo single,3 --mac --switch ovsk --controller remote
```

---

### Step 3: Test Connectivity

```bash
h1 ping -c 5 h3
h2 ping -c 5 h3
```

---

### Step 4: Verify Flow Rules

```bash
sh ovs-ofctl dump-flows s1
```

---

## Observations

* All hosts can communicate successfully
* Flow table shows different priorities:

  * `priority=100` for h1
  * `priority=10` for h2
* Ping latency is similar due to lack of real congestion in Mininet

---


---

##  Limitations

* Mininet does not simulate real network congestion
* QoS effect is visible in flow rules, not latency

---

##  Future Improvements

* Add bandwidth control using `tc`
* Implement dynamic QoS policies
* Extend to multiple switches
* Integrate real-time traffic monitoring

---

##  Conclusion

This project successfully demonstrates how SDN can be used to implement QoS by assigning different priorities to traffic flows using OpenFlow rules. It highlights the flexibility and programmability of SDN-based networks.

---

## 📊 Scalability Performance Evaluation

To evaluate the scalability of the QoS controller, the system behavior is analyzed for increasing number of hosts. Due to system limitations, large-scale results are theoretical and based on expected SDN behavior.

### 🔢 Test Scenarios

* Small scale → 10 hosts
* Medium scale → 100 hosts
* Large scale → 1000 hosts
* Very large scale → 10000 hosts

---

### 📋 Performance Table

```
+------------+------------------+----------------------+------------------------+-----------------------------+
| Hosts      | Flow Entries     | Controller Load      | Avg Latency (Expected) | QoS Effectiveness           |
+------------+------------------+----------------------+------------------------+-----------------------------+
| 10         | ~20              | Low                  | ~0.2 ms                | Clearly visible             |
| 100        | ~200             | Moderate             | ~0.5 ms                | Maintained                  |
| 1000       | ~2000            | High                 | ~1–2 ms                | Slight degradation          |
| 10000      | ~20000           | Very High            | ~5–10 ms               | Reduced but functional      |
+------------+------------------+----------------------+------------------------+-----------------------------+
```

---

### 📈 Observations

* Flow table size increases linearly with number of hosts
* Controller processing load increases significantly at scale
* Latency increases due to control overhead
* QoS priority mechanism continues to function correctly

---

---

## 📸 Screenshots
<img width="830" height="239" alt="WhatsApp Image 2026-04-20 at 12 07 38 AM" src="https://github.com/user-attachments/assets/525a3ac0-e772-4a21-b05c-71efc75f41ce" />
<img width="392" height="86" alt="WhatsApp Image 2026-04-20 at 12 08 32 AM" src="https://github.com/user-attachments/assets/b8ccf560-4114-4077-8d10-de33f4d3829d" />
<img width="652" height="162" alt="WhatsApp Image 2026-04-20 at 12 08 59 AM" src="https://github.com/user-attachments/assets/32ac6e97-e729-4886-8b57-c55172ca86eb" />
<img width="840" height="310" alt="WhatsApp Image 2026-04-20 at 12 38 19 AM" src="https://github.com/user-attachments/assets/c071afc0-d8b8-4f03-b33c-ce17e65163c6" />





