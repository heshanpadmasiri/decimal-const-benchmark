test: $(addsuffix .exe, $(basename $(wildcard *.bal)))

%.exe: %.bc %._init.bc
	clang-12 -O0 -g -o $@ $^ balrt.a

%.bc: %.ll
	llvm-link-12 -o $@ $< balrt_inline.bc

clean:
	rm -rf *.bc
	rm -rf *.exe
	ln -s ../nballerina/runtime/balrt_inline.bc .
