package injector

import (
	"syscall"

	"github.com/TheTitanrain/w32"
)

func main() {
	dllPath := `PATHTO\test.dll`

	dllPathUTF16, err := syscall.UTF16PtrFromString(dllPath)
	if err != nil {
		panic(err)
	}

	syscall.GetFullPathName()

	handle, err := w32.OpenProcess(w32.PROCESS_CREATE_THREAD|
		w32.PROCESS_QUERY_INFORMATION|
		w32.PROCESS_VM_OPERATION|
		w32.PROCESS_VM_READ|
		w32.PROCESS_VM_READ,
		false,
		6896) // That's a random PID

	if err != nil {
		panic(err)
	}

	hFile, err := sys.o
	if err != nil {
		panic(err)
	}
}
