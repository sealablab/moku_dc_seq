-- (missing?) Clk-n-reg example 10 from vhdl by readler

library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;

entity clk_n_reg_4 is 
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
end entity clk_n_reg_4;


-- Architcture block 
architecture clk_n_reg_4_arch of clk_n_reg_4 is
	--- intermediate signal definitions 
	signal cnt_en	: std_logic;
	signal count_us	: unsigned(3 downto 0);

begin
	cnt_en <= '1';	
	
end architecture;

