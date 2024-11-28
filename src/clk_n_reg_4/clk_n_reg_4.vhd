-- (missing?) Clk-n-reg example 10 from vhdl by readler

library ieee;
use ieee.std_logic_1164.all;

entity clk_n_regs_4 is 
  port (
		 -- Inputs
		clk		: in std_logic;
		rst		: in std_logic;
		
		start	: in std_logic;
		stop	: in std_logic;

		-- Outputs
		count	: out std_logic_vector(3 downto 0);
		stop_d2	: out std_logic
    );
end clk_n_regs_4;

architecture arch of clk_n_regs_4 is
begin
	-- code goes here
end arch;

