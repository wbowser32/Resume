import java.awt.*;
import javax.swing.*;
import java.awt.event.*;

public class Emergency extends JFrame implements ActionListener {
    JButton remindersButton;
    JButton lifehacksButton;
    JButton helpfulhintsButton;
    JTextArea textArea;
    
    public Emergency() {
        super("Helpful?");
        setLookAndFeel();
        setSize(500, 400);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        FlowLayout flo = new FlowLayout();
        setLayout(flo);
        remindersButton =new JButton("Reminders");
        lifehacksButton = new JButton ("Life Hacks");
        helpfulhintsButton = new JButton ("Helpful Hints");
        textArea = new JTextArea ("Oh Boy");
        remindersButton.addActionListener(this);
        lifehacksButton.addActionListener(this);
        helpfulhintsButton.addActionListener(this);
        
        JPanel p = new JPanel();
        JPanel[] panels = new JPanel[3];
        for( int i = 0 ; i < panels.length; i++)
        {
            panels[i] = new JPanel();
        }
        
        panels[0].add(remindersButton);
        add(panels[0], flo);
        
        panels[1].add(lifehacksButton);
        add(panels[1], flo );
        
        panels[2].add(helpfulhintsButton);
        add(panels[2], flo);
        add(textArea,flo);
        setVisible(true);
    }
    
    private void setLookAndFeel() 
    {
        try 
        {
            UIManager.setLookAndFeel
            (
                "com.sun.java.swing.plaf.nimbus.NimbusLookAndFeel"
            );  
            int x = 1;
        } 
        catch (Exception exc) 
        {
            int x = 1;
            //ignore error
        }
    }
   
    public void actionPerformed(ActionEvent e)
    {
        String nText="";
        if(e.getSource() == remindersButton)
        {
            nText = ("Be Kind to All. Be Sure to see life from all points. Never give up");
        }
        else if(e.getSource() == lifehacksButton)
        {
            nText = ("You are on your own");
        }
         else if(e.getSource() == helpfulhintsButton)
        {
            nText = ("When in doubt Google it");
        }
        textArea.setText(nText);
    }
    
    public static void main(String[] args)
    {
        Emergency cr = new Emergency();
    }
}

    
