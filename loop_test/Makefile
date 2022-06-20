tests=$(basename $(wildcard *.bal))
compile_output=$(addsuffix .bal.md, $(tests))
run_output=$(addsuffix .exe.md, $(tests))
old_exe=$(addsuffix _old.exe, $(tests))
new_exe=$(addsuffix _old.exe, $(tests))

%.exe: %.bc %._init.bc
	clang-12 -O0 -g -o $@ $^ balrt.a

%.bc: %.ll
	llvm-link-12 -o $@ $< balrt_inline.bc

clean:
	rm -rf *.exe
	rm -rf *.ll
	rm nballerina.jar
	rm balrt_inline.bc
	rm balrt.a

%.bal.md: %.bal
	hyperfine --show-output --export-markdown $@ "java -jar nballerina_new.jar $<" "java -jar nballerina_old.jar $<"

%.exe.md: %_old.exe %_new.exe
	hyperfine -N --export-markdown $@ "./$<" "./$(word 2,$^)"

%_old.exe: %.bal
	java -jar nballerina_old.jar $<
	llvm-link-12 -o $*.bc $*.ll balrt_inline_old.bc
	llvm-link-12 -o $*._init.bc $*._init.ll balrt_inline_old.bc
	clang-12 -O0 -g -o $@ $*.bc $*._init.bc balrt_old.a

%_new.exe: %.bal
	java -jar nballerina_new.jar $<
	llvm-link-12 -o $*.bc $*.ll balrt_inline_new.bc
	llvm-link-12 -o $*._init.bc $*._init.ll balrt_inline_new.bc
	clang-12 -O0 -g -o $@ $*.bc $*._init.bc balrt_new.a

compile: $(sort $(compile_output))

run: $(sort $(run_output))

switch_new:
	ln -s nballerina_new.jar nballerina.jar
	ln -s balrt_inline_new.bc balrt_inline.bc
	ln -s balrt_new.a balrt.a

switch_old:
	ln -s nballerina_old.jar nballerina.jar
	ln -s balrt_inline_old.bc balrt_inline.bc
	ln -s balrt_old.a balrt.a
