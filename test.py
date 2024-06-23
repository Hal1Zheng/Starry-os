import matplotlib.pyplot as plt

# Define the sections and their sizes for the memory layout
sections = [
    (".text", 0x4000),
    (".rodata", 0x4000),
    (".data", 0x4000),
    (".tdata", 0x10),
    (".tbss", 0x10),
    (".sigtrx", 0x4000),
    (".percpu", 0x1000),
    (".bss", 0x4000)
]

# Start address
base_address = 0x80000000

# Initialize memory layout
memory_layout = []
current_address = base_address

for section, size in sections:
    memory_layout.append((current_address, section, size))
    current_address += size

# Create the figure and axis
fig, ax = plt.subplots(figsize=(12, 8))

# Plot the memory layout
for address, section, size in memory_layout:
    ax.barh(section, size, left=address - base_address, color='skyblue')
    ax.text(address - base_address + size / 2, section, f"{section} ({hex(address)})", 
            ha='center', va='center', color='black')

# Format the plot
ax.set_xlabel('Memory Address Offset')
ax.set_title('Kernel Memory Layout')
ax.grid(True)

plt.tight_layout()
plt.show()
