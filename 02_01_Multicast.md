# IP Multicasting
## Concept
* Packets are routed from **source** to **multiple destinations**
* Used for group communication such as videoconferencing, video broadcasting
* The **Address** identifies a group instead of a single host
## Addressing
* It uses **Class D** address
	* Beginning with 1110 -> with a range from **224.0.0.0** to **239.255.255.255**
* Packets are delivered to every host in the group(Anywhere in the network)
## Host Group
* Hosts join and leave dynamically.
* **Recipients** establish which hosts receive a packet.
	* Different than in unicast where the **source** decides.
	* Controlling traffic reach is more difficult.
* The recipient can join:
	* Having the group's IP address, inform the rooter that it want to join.
## Within an IEEE 802 Network
* The group delivery is delegated to a lower level(MAC)
* First to receive from the group. The recipient has to go to the link layer.
* The IP multicast address is mapped to a MAC multicast address.
	![](img/2022-02-05-22-37-10.png) 
	* 28 bits out of 32 are unique for the IP address
	![](img/2022-02-05-22-38-26.png)
	* While for the Mac addresses reserved for Multicast starts with 01-00-5E-0. Therefore we have an overlap of 5 bit bits that has to be cut from the IP address
	* 23 least significat bit should contain the IP address
* The interface card has to be configured to receive that MAC multicast
	* Recipient initiated group join event
* A packet sent to that address is received by all joined hosts
## Beyond a Single Network
* Routers discover host groups on each LAN
	* IGMP (Internet Group Management Protocol) makes possible for the nodes to tell the default gateway to forward the contnt if you want to subscribe to a multicast group.
* Routers announce host groups to others: To make possible to share if no one is interested between routers
* Routers build a distribution tree for each host group -> to all LANs with at least one member
## State of Deployment
* Not widely supported
* Not fit to common traffic control/engineering practices
* Mostly limited controlled environments (eg. video broadcasting over IP solutions)
