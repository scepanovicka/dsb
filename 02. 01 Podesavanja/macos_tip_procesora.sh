# ova skripta je namenjena samo za macOS
# ⚠️ ne koristiti na Windows ili Linux masinama

arch_name="$(uname -m)"

if [ "${arch_name}" = "x86_64" ]; then
    if [ "$(sysctl -in sysctl.proc_translated)" = "1" ]; then
        echo "Tvoj kompjuter koristi Apple Silicon (Rosetta) 🌟"
    else
        echo "Tvoj kompjuter koristi Intel procesor 🤖"
    fi
elif [ "${arch_name}" = "arm64" ]; then
    echo "Tvoj kompjuter koristi Apple Silicon 🌟"
else
    echo "Greska: ${arch_name}, kontaktiraj trenera 🤔"
fi
