    # implement method to do the work, "state" is the internal compiler
    # state from the CompilerBase instance.
    def run_pass(self, state):
        func_ir = state.func_ir # get the FunctionIR object
        mutated = False # used to record whether this pass mutates the IR
        # walk the blocks
        for blk in func_ir.blocks.values():
            # find the assignment nodes in the block and walk them
            for assgn in blk.find_insts(ir.Assign):
                # if an assignment value is a ir.Consts
                if isinstance(assgn.value, ir.Const):
                    const_val = assgn.value
                    # if the value of the ir.Const is a Number
                    if isinstance(const_val.value, Number):
                        # then add one!
                        const_val.value += 1
                        mutated |= True
        return mutated # return True if the IR was mutated, False if not.
