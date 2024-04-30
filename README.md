# PRODIGY_CS_05
# Network Packet Analyzer
Alright, imagine you're sitting at a control center, monitoring all the traffic coming in and out of a network. This code is like your assistant, a packet sniffer, helping you keep track of all the network packets flying around. 

When you start the program, it cheerfully announces, "Packet Sniffer started..." to let you know it's up and running. It then quietly listens to all the network traffic, ready to analyze any packets it comes across.

Now, imagine a packet as a small envelope containing important information. Each time the sniffer detects an "IP" layer in a packet (which is like the address on the envelope indicating where it's coming from and where it's going), it perks up and starts analyzing the contents.

The `packet_callback` function is like the brain of this assistant. It quickly opens the envelope (the packet) and takes note of the source IP address (where the packet is coming from), the destination IP address (where it's going), the protocol (the type of communication used, like TCP or UDP), and even the payload data (the actual message or data inside the packet).

Once it has all this information, it excitedly prints it out for you to see. You'll get to know the source and destination IP addresses, the protocol being used, and a sneak peek at the payload data. It's like your assistant eagerly showing you what's inside each envelope as it arrives.

This program keeps running in the background, quietly sniffing out packets and analyzing them for you. It's like having a diligent assistant constantly on the lookout, making sure everything is running smoothly in your network control center.
