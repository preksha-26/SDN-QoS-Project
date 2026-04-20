from pox.core import core
import pox.openflow.libopenflow_01 as of
from pox.lib.util import dpid_to_str
from pox.lib.addresses import EthAddr

log = core.getLogger()


def _handle_ConnectionUp(event):
    log.info("Switch %s connected", dpid_to_str(event.dpid))

    # High priority: h1 -> h3
    msg1 = of.ofp_flow_mod()
    msg1.priority = 100
    msg1.match.in_port = 1
    msg1.actions.append(of.ofp_action_output(port=3))
    event.connection.send(msg1)

    # Low priority: h2 -> h3
    msg2 = of.ofp_flow_mod()
    msg2.priority = 10
    msg2.match.in_port = 2
    msg2.actions.append(of.ofp_action_output(port=3))
    event.connection.send(msg2)

    # Return traffic: h3 -> h1
    msg3 = of.ofp_flow_mod()
    msg3.priority = 100
    msg3.match.in_port = 3
    msg3.match.dl_dst = EthAddr("00:00:00:00:00:01")
    msg3.actions.append(of.ofp_action_output(port=1))
    event.connection.send(msg3)

    # Return traffic: h3 -> h2
    msg4 = of.ofp_flow_mod()
    msg4.priority = 10
    msg4.match.in_port = 3
    msg4.match.dl_dst = EthAddr("00:00:00:00:00:02")
    msg4.actions.append(of.ofp_action_output(port=2))
    event.connection.send(msg4)


def launch():
    core.openflow.addListenerByName("ConnectionUp", _handle_ConnectionUp)
