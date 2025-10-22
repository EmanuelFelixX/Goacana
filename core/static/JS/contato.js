function enviarWhats(){
    const nome = document.getElementById('nome').value;
    const assunto = document.getElementById('assunto').value;
    const msg = document.getElementById('mensagem').value;
    const usertel = document.getElementById('telefone').value;
    const useremail = document.getElementById('email').value;
    const telefone = '558491061685';
    const mensagem = `Olá, meu nome é ${nome}. Gostaria de falar sobre ${assunto}.`;
    const msgFormatada = encodeURIComponent(mensagem);
    const url = `https://wa.me/${telefone}?text=${msgFormatada}`;
    window.open(url, '_blank');
}
